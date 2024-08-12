import os
from webdriver_manager.chrome import ChromeDriverManager
from pinnacle import get_pin_odds
from tab import get_tab_odds
from sportsbet import get_sb_odds
from helper import convert_odds
from match_events import get_pos_ev
from link_manager import links
from selenium.common.exceptions import WebDriverException

def main():
    # Install chrome driver in current directory
    os.environ['WDM_LOCAL'] = '1'
    driver_path = ChromeDriverManager().install()

    for link in links.values():
        try:
            pin_odds = convert_odds(get_pin_odds(driver_path, link['pin']))
            tab_odds = get_tab_odds(driver_path, link['tab'])
            sb_odds = get_sb_odds(driver_path, link['sb'])
        except WebDriverException:
            continue
        print(get_pos_ev(pin_odds, tab_odds))
        print(get_pos_ev(pin_odds, sb_odds))

if __name__ == '__main__':
    main() 