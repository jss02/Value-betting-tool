# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta, time

# Temporary link
web = 'https://www.tab.com.au/sports/betting/AFL%20Football'

"""
get_tab_odds(driver_path)

Scrapes the game time, odds, and team names from tab.com.au and returns it as a list of game dictionaries

Params:
    driver_path (str): relative path of chromedriver.

Returns:
    list: list of dictionary containing game information
"""
def get_tab_odds(driver_path):

    # Set webdriver options
    driver_options = Options()
    #driver_options.add_argument("--headless") tab blocks headless mode
    driver_options.add_argument('log-level=3')

    # Set up webdriver
    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    # Open URL
    driver.get(web)

    # list for storing games and their information
    games = []

    # Get all events and iterate through them
    driver.get_screenshot_as_file("screenshot.png")
    events = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, "customised-template")))
    for row in events.find_elements(By.XPATH, "./*"):
        # If game is live, skip
        if "live" in row.get_attribute('class'):
            continue
        
        game_details = {}

        # Get match name and store team names
        matchname = row.find_element(By.CLASS_NAME, "match-name-text").text
        game_details['name'] = matchname
        game_details['team1'], game_details['team2'] = [x.strip() for x in matchname.split(' v ', 1)]

        # Get game time and add to dict as datetime object
        try:
            gametime = row.find_element(By.CSS_SELECTOR, "[data-test='close-time']").text
            game_details['datetime'] = datetime.strptime(gametime, "%a %d %b %H:%M").replace(year=datetime.now().year)
        except NoSuchElementException:
            # If element isn't found, then even is suspended and skip
            continue
        
        # Iterate through columns and save odds into a list
        columns = row.find_element(By.CLASS_NAME, "propositions-wrapper")
        odds = []
        for col in columns.find_elements(By.XPATH, "./*"):

            # Check if column odds market
            market = col.find_element(By.CLASS_NAME, "proposition-bet-option").get_attribute('data-content')
            # Skip if the market is Line as some sports also display line along with Head To Head
            if market == "Line":
                continue
            
            # Add odd to list of odds if it isn't the Line odds
            odds.append(col.find_element(By.CLASS_NAME, "animate-odd").text)

        # Skip if there isn't more than one odd
        if len(odds) < 2: 
            continue
        
        # Add win-draw-win odds to dict
        if len(odds) == 3:
            game_details['team1_odds'], game_details['draw'], game_details['team2_odds'] = odds

        # Or add win-win odds to dict
        else:
            game_details['team1_odds'], game_details['team2_odds'] = odds
        
        # Append dict to list
        games.append(game_details)

    return games
       
if __name__ == '__main__':
    print(get_tab_odds(None))