# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, time

# Helper function that converts given date string to datetime object
def format_date(date):
    if "today" in date.text.lower():
        return datetime.combine(datetime.today(), time(0, 0))
    elif "tomorrow" in date.text.lower():
        return datetime.combine(datetime.today() + timedelta(days=1), time(0, 0))
    else:
        return datetime.strptime(date.find('span').text.split(', ', 1)[1], '%b %d, %Y')

"""
get_pin_odds(driver_path)

Scrapes the game time, odds, and team names from pinnacle.com and returns it as a list of game dictionaries

Params:
    driver_path (str): relative path of chromedriver.

Returns:
    List[Dict]: list of dictionary containing game information
    - sorted in order of game time since they are scraped in the order displayed by the website
      which is already sorted
"""
def get_pin_odds(driver_path, web):

    # Set webdriver options
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver_options.add_argument('log-level=3')
    driver_options.add_argument('window-size=1920x1080')

    # Set up webdriver
    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    # Open URL
    driver.get(web)

    # Wait until webdriver finds content block containing the games
    WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.square")))

    # driver.get_screenshot_as_file("pin.png") # Take screenshot of current page for debugging

    # Get page and close driver
    page_source = driver.page_source
    driver.quit()

    # Parse with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Get list of events
    events = soup.select_one("div.contentBlock.square")
    
    # list for storing games and their information
    games = []

    # Get all rows of events and iterate through them
    for row in events.children:
        # If row is a row containing the date only, set date
        if "dateBar" in ' '.join(row.get('class', [])):
            game_datetime = format_date(row)
        else:
        # Else it either contains the game information or market label (1 x 2, handicap, O/U etc.)
            game_details = {}

            # Iterate through columns of row to extract 
            for col in row.children:
                # If column contains metadata (team names and game time)
                if "metadata" in ' '.join(col.get('class', [])):
                    # Add team names to dict
                    game_info = col.find_all('span')
                    game_details['team1'] = game_info[0].text.split('(')[0].strip()
                    game_details['team2'] = game_info[1].text.split('(')[0].strip()

                    # Add time to game_datetime datetime object and add to dict
                    hrs, mins = map(int, game_info[2].text.split(':'))
                    game_details['datetime'] = game_datetime.replace(hour=hrs, minute=mins)
                
                # Else if it contains moneyline odds
                elif "moneyline" in ' '.join(col.get('class', [])):
                    # Get odds
                    odds = col.find_all('span')

                    # Skip if game odds are suspended or unavailable
                    if len(odds) < 2:
                        break

                    # Add win-draw-win odds to dict
                    if len(odds) > 2:
                        game_details['team1_odds'] = float(odds[0].text)
                        game_details['draw'] = float(odds[1].text)
                        game_details['team2_odds'] = float(odds[2].text)

                    # Or add win-win odds to dict
                    else:
                        game_details['team1_odds'] = float(odds[0].text)
                        game_details['team2_odds'] = float(odds[1].text)

                    # Append dict to list
                    games.append(game_details)

                    break # Move to next row as we only want moneyline odds
                       
    return games

if __name__ == '__main__':
    print(get_pin_odds(None, 'https://www.pinnacle.com/en/rugby-league/nrl/matchups/#period:0'))