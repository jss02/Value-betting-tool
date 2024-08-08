# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from datetime import datetime

# Temporary link
web = 'https://www.tab.com.au/sports/betting/Soccer/competitions/English%20Premier%20League'

"""
get_tab_odds(driver_path)

Scrapes the game time, odds, and team names from tab.com.au and returns it as a list of game dictionaries

Params:
    driver_path (str): relative path of chromedriver.

Returns:
    List[Dict]: list of dictionary containing game information
    - sorted in order of game time since they are scraped in the order displayed by the website
      which is already sorted
"""
def get_tab_odds(driver_path):

    # Set webdriver options
    driver_options = Options()
    # driver_options.add_argument("--headless") #tab blocks headless mode
    driver_options.add_argument('log-level=3')

    # Set up webdriver
    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    # Open URL
    driver.get(web)

    # Wait until webdriver finds element containing the games
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "customised-template")))

    driver.get_screenshot_as_file("tab.png") # Take screenshot of current page for debugging
    
    # Get page and close driver
    page_source = driver.page_source
    driver.quit()

    # Parse with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Get list of events
    events = soup.find('div', class_=["customised-template"])

    # list for storing games and their information
    games = []

    # Get all events and iterate through them
    for row in events.find_all('div', class_='template-item'):
        # If game is live, skip
        if "live" in ' '.join(row.get('class', [])):
            continue
        
        game_details = {}

        # Get match name and store team names
        matchname = row.find('span', class_="match-name-text").text
        game_details['name'] = matchname
        game_details['team1'], game_details['team2'] = [x.strip() for x in matchname.split(' v ', 1)]

        # Get game time and add to dict as datetime object
        try:
            gametime = row.find('li', {'data-test': 'close-time'}).text
            game_details['datetime'] = datetime.strptime(gametime, "%a %d %b %H:%M").replace(year=datetime.now().year)
        except NoSuchElementException:
            # If element isn't found, then even is suspended and skip
            continue
        
        # Iterate through columns and save odds into a list
        columns = row.find('div', class_="propositions-wrapper")
        odds = []
        for col in columns.find_all('div', class_='proposition-wrapper'):

            # Check if column odds market
            market = col.find('span', class_="proposition-bet-option").get('data-content')
            # Skip if the market is Line as some sports also display the Line along with Head To Head
            if market == "Line":
                continue
            
            # Add odd to list of odds if it isn't the Line odds
            odds.append(float(col.find('div', class_="animate-odd").text))

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