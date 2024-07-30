# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, time

# Temporary link
web = "https://www.pinnacle.com/en/soccer/england-premier-league/matchups/#all"

# Helper function that converts given date string to datetime object
def format_date(date):
    if "TODAY" in date.text:
        return datetime.combine(datetime.today(), time(0, 0))
    elif "TOMORROW" in date.text:
        return datetime.combine(datetime.today() + timedelta(days=1), time(0, 0))
    else:
        return datetime.strptime(date.find_element(By.TAG_NAME, 'span').text.split(', ', 1)[1], '%b %d, %Y')

"""
get_pin_odds(driver_path)

Scrapes the game time, odds, and team names from pinnacle.com and returns it as a list of game dictionaries

Params:
    driver_path (str): relative path of chromedriver.

Returns:
    list: list of dictionary containing game information
"""
def get_pin_odds(driver_path):

    # Set webdriver options
    driver_options = Options()
    #driver_options.add_argument("--headless")

    # Set up webdriver
    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    # Open URL
    driver.get(web)

    # Wait until webdriver finds content block containing the games
    events = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'contentBlock square')]")))

    # list for storing games and their information
    games = []

    # Get all rows of events and iterate through them
    rows = events.find_elements(By.XPATH, "./*")
    for row in rows:
        # If row is a row containing the date only, set date
        if "dateBar" in row.get_attribute('class'):
            game_datetime = format_date(row)
        
        # Else it either contains the game information or market label (1 x 2, handicap, O/U etc.)
        else:
            game_odds = {}

            # Iterate through columns of row to extract 
            columns = row.find_elements(By.XPATH, "./*")
            for col in columns:
                # If column contains metadata (team names and game time)
                if "metadata" in col.get_attribute('class'):
                    # Add team names to dict
                    game_info = col.find_elements(By.TAG_NAME, 'span')
                    game_odds['team1'] = game_info[0].text.split('(')[0].strip()
                    game_odds['team2'] = game_info[1].text.split('(')[0].strip()

                    # Add time to game_datetime datetime object and add to dict
                    hrs, mins = map(int, game_info[2].text.split(':'))
                    game_odds['datetime'] = game_datetime.replace(hour=hrs, minute=mins)
                
                # Else if it contains moneyline odds
                elif "moneyline" in col.get_attribute('class'):
                    # Get odds
                    odds = col.find_elements(By.TAG_NAME, 'span')

                    # Skip if game odds are suspended or unavailable
                    if len(odds) < 2:
                        break

                    # Add win-draw-win odds to dict
                    if len(odds) > 2:
                        game_odds['team1_odds'] = odds[0].text
                        game_odds['draw'] = odds[1].text
                        game_odds['team2_odds'] = odds[2].text

                    # Or add win-win odds to dict
                    else:
                        game_odds['team1_odds'] = odds[0].text
                        game_odds['team2_odds'] = odds[1].text

                    # Append dict to list
                    games.append(game_odds)

                    break # Move to next row as we only want moneyline odds
                    
    driver.quit()

    return games