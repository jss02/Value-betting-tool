# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import re

# Temp link
web = 'https://www.sportsbet.com.au/betting/soccer/united-kingdom/english-premier-league'

"""
get_sb_odds(driver_path)

Scrapes the game time, odds, and team names from sportsbet.com.au and returns it as a list of game dictionaries

Params:
    driver_path (str): relative path of chromedriver.

Returns:
    list: list of dictionary containing game information
    - games are sorted in order of game time since they are scraped in the order displayed by the website
      which is already sorted
"""
def get_sb_odds(driver_path):

    # Set webdriver options
    driver_options = Options()
    # driver_options.add_argument("--headless")
    driver_options.add_argument('log-level=3')

    # Set up webdriver
    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    # Open URL
    driver.get(web)

    # list for storing games and their information
    games = []

    driver.get_screenshot_as_file("sb.png") # Take screenshot of current page for debugging

    # Get list of events and iterate through them
    events = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-automation-id='competition-matches-container']")))
    for event in events.find_elements(By.TAG_NAME, 'li'):

        # Check if <time> element is present, otherwise it is a live game
        gametime_list = event.find_elements(By.TAG_NAME, 'time')
        if gametime_list:
            # Although time is given in ISO 8601 format, there is a known python3.10 bug that gives format error
            # when fractional seconds are given in 4 decimals, so we must regex and then convert
            match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})', gametime_list[0].get_attribute('datetime')).group(1)
            gametime = datetime.strptime(match, '%Y-%m-%dT%H:%M:%S')
        else:
            continue # Skip game
        
        # Get game link
        game_link = event.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # Initialise dict containing game information
        game_details = {'datetime': gametime, 'link': game_link}

        # Find if h2 element containing game title is present within the event, if not then it is a multi market
        # container meaning it is in a different structure to a single market container
        matchname = event.find_elements(By.TAG_NAME, 'h2')
        if matchname:
            game_details['name'] = matchname[0].text
            for i, outcome in enumerate(event.find_elements(By.TAG_NAME, 'Button')):

                # Note that the first <span> collected is a container with no text
                texts = outcome.find_elements(By.TAG_NAME, 'span')

                # If there is 3 outcomes (draw), then set appropriate changes
                if i == 2:
                    game_details[f"team{i}"] = texts[1].text
                    game_details[f"team{i}_odds"], game_details['draw'] = float(texts[2].text), game_details[f"team{i}_odds"]
                else:
                    game_details[f"team{i+1}"] = texts[1].text
                    game_details[f"team{i+1}_odds"] = float(texts[2].text)
        else:
            pass
        
        games.append(game_details)

    return games

if __name__ == '__main__':
    print(get_sb_odds(None))