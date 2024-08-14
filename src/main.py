from webdriver_manager.chrome import ChromeDriverManager
from pinnacle import get_pin_odds
from tab import get_tab_odds
from sportsbet import get_sb_odds
from helper import convert_odds
from match_events import get_pos_ev
from link_manager import links
from selenium.common.exceptions import WebDriverException

def main(sb=True, tab=True):
    driver_path = ChromeDriverManager().install()

    for link in links.values():
        try:
            pin_odds = convert_odds(get_pin_odds(driver_path, link['pin']))
            if tab:
                tab_odds = get_tab_odds(driver_path, link['tab'])
            if sb:
                sb_odds = get_sb_odds(driver_path, link['sb'])
        except WebDriverException:
            print(f'Error scraping {link}')
            continue
        print(get_pos_ev(pin_odds, tab_odds), link['tab'])
        print(get_pos_ev(pin_odds, sb_odds), link['sb'])

# Option to run main without tab
def not_tab():
    main(tab=False)

if __name__ == '__main__':
    main()