# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, time
import re

web = "https://www.pinnacle.com/en/soccer/england-premier-league/matchups/#all"

# Function that formats the date to
def format_date(date):
    if "TODAY" in date.text:
        return datetime.combine(datetime.today(), time(0, 0))
    elif "TOMORROW" in date.text:
        return datetime.combine(datetime.today() + timedelta(days=1), time(0, 0))
    else:
        return datetime.strptime(date.find_element(By.TAG_NAME, 'span').text.split(', ', 1)[1], '%b %d, %Y')

def get_pin_odds(driver_path):
    driver_options = Options()
    #driver_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)

    driver.get(web)

    # Wait until webdriver finds content block
    events = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'contentBlock square')]")))

    # Store games and their odds
    games = []

    # Get all rows of events
    rows = events.find_elements(By.XPATH, "./*")
    for row in rows:
        if "dateBar" in row.get_attribute('class'):
            game_datetime = format_date(row)
        else:
            game_odds = {}
            columns = row.find_elements(By.XPATH, "./*")
            for col in columns:
                if "metadata" in col.get_attribute('class'):
                    game_info = col.find_elements(By.TAG_NAME, 'span')
                    game_odds['team1'] = game_info[0].text.split('(')[0].strip()
                    game_odds['team2'] = game_info[1].text.split('(')[0].strip()

                    hrs, mins = map(int, game_info[2].text.split(':'))
                    game_odds['datetime'] = game_datetime.replace(hour=hrs, minute=mins)
                elif "moneyline" in col.get_attribute('class'):
                    odds = col.find_elements(By.TAG_NAME, 'span')
                    if len(odds) < 2:
                        break
                    # 1 x 2
                    if len(odds) > 2:
                        game_odds['team1_odds'] = odds[0].text
                        game_odds['draw'] = odds[1].text
                        game_odds['team2_odds'] = odds[2].text

                    # No draw 
                    else:
                        game_odds['team1_odds'] = odds[0].text
                        game_odds['team2_odds'] = odds[1].text

                    games.append(game_odds)

                    break
            
    print(games)
                    
    driver.quit()
