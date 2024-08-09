# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import re

"""
get_sb_odds(driver_path)

Scrapes the game time, odds, and team names from sportsbet.com.au and returns it as a list of game dictionaries

Params:
    driver_path (str): relative path of chromedriver.

Returns:
    List[Dict]: list of dictionary containing game information
    - sorted in order of game time since they are scraped in the order displayed by the website
      which is already sorted
"""
def get_sb_odds(driver_path, web):

    # Set webdriver options
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver_options.add_argument('log-level=3')

    # Set up webdriver
    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    # Open URL
    driver.get(web)

    # list for storing games and their information
    games = []

    # List of markets that we want to scrape
    market_names = ["Head to Head", "Match Betting", "Money Line"]

    driver.get_screenshot_as_file("sb.png") # Take screenshot of current page for debugging

    # Get list of events and iterate through them
    events = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-automation-id='competition-matches-container']")))
    for event in events.find_elements(By.TAG_NAME, 'li'):

        # Check if <time> element is present, otherwise it is a live game
        gametime_list = event.find_elements(By.TAG_NAME, 'time')
        if gametime_list:
            # Although time is given in ISO 8601 format, there is a known python3.10 bug that gives format error
            # when fractional seconds are given in 4 decimals, so we must regex and then convert to datetime
            match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})', gametime_list[0].get_attribute('datetime')).group(1)
            gametime = datetime.strptime(match, '%Y-%m-%dT%H:%M:%S')
        else:
            continue # Skip game

        # Initialise dict containing game information
        game_details = {'datetime': gametime}

        # Find if h2 element containing game title is present within the event, if not then it is a multi market
        # container meaning it is in a different structure to a single market container
        matchname = event.find_elements(By.TAG_NAME, 'h2')
        if matchname:
            game_details['name'] = matchname[0].text
            for i, outcome in enumerate(event.find_elements(By.TAG_NAME, 'Button')):

                # Note that the first <span> collected is a container with no text
                texts = outcome.find_elements(By.TAG_NAME, 'span')

                # Add team and odds to game dict
                if i == 2:
                    # If 3 outcomes are present, create a 'draw' key value pair and swap previous key value with current
                    # since previous iteration would've been the draw outcome
                    game_details[f"team{i}"] = texts[1].text
                    game_details[f"team{i}_odds"], game_details['draw'] = float(texts[2].text), game_details[f"team{i}_odds"]
                else:
                    game_details[f"team{i+1}"] = texts[1].text
                    game_details[f"team{i+1}_odds"] = float(texts[2].text)
        else:
        # Scraping for multi market containers
            # Add team names to dict
            game_details['team1'] = event.find_element(By.CSS_SELECTOR, '[data-automation-id="participant-one"]').text
            game_details['team2'] = event.find_element(By.CSS_SELECTOR, '[data-automation-id="participant-two"]').text
            game_details['name'] = game_details['team1'] + ' v ' + game_details['team2']
            
            # Get grid of markets and iterate through them
            market_grid = event.find_element(By.CLASS_NAME, 'market-coupon-grid')
            found = False # Boolean to check if desired market is present
            for market in market_grid.find_elements(By.XPATH, "./*"):
                # If current market is Head to head, Match betting, or Money line then add to dict and break
                if market.find_element(By.CSS_SELECTOR, '[data-automation-id="market-coupon-label"]').text in market_names:
                    odds = market.find_elements(By.CSS_SELECTOR, '[data-automation-id="price-text"]')
                    game_details['team1_odds'], game_details['team2_odds'] = float(odds[0].text), float(odds[1].text)
                    found = True
                    break
            
            # If desired market wasn't found, don't add to return list and continue
            if not found:
                continue
        
        games.append(game_details)

    return games

if __name__ == '__main__':
    print(get_sb_odds(None, 'https://www.sportsbet.com.au/betting/rugby-league/nrl'))