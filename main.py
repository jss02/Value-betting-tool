import os
from webdriver_manager.chrome import ChromeDriverManager
from pinnacle import get_pin_odds
from tab import get_tab_odds
from helper import convert_odds

def main():
    # Install chrome driver in current directory
    os.environ['WDM_LOCAL'] = '1'
    driver_path = ChromeDriverManager().install()

    pin_odds = convert_odds(get_pin_odds(driver_path))
    tab_odds = get_tab_odds(driver_path)


if __name__ == '__main__':
    main() 