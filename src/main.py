from webdriver_manager.chrome import ChromeDriverManager
from pinnacle import get_pin_odds
from tab import get_tab_odds
from sportsbet import get_sb_odds
from helper import convert_odds
from match_events import get_pos_ev
from link_manager import links
import sys
from decorators import get_decorator

def main(sb=True, tab=True):
    driver_path = ChromeDriverManager().install()

    for league, link in links.items():
        # Links are passed as lambda functions for decorator KeyError handling
        pin_odds = get_decorator(get_pin_odds)(driver_path, lambda: link['pin'])
        if not pin_odds:
            print(f"Skipping {league}", file=sys.stderr)
            continue
        pin_odds = convert_odds(pin_odds)
        if tab:
            tab_odds = get_decorator(get_tab_odds)(driver_path, lambda: link['tab'])
            if tab_odds:
                print(get_pos_ev(pin_odds, tab_odds), link['tab'])
        if sb:
            sb_odds = get_decorator(get_sb_odds)(driver_path, lambda: link['sb'])
            if sb_odds:
                print(get_pos_ev(pin_odds, sb_odds), link['sb'])
        
# Option to run main without tab
def not_tab():
    main(tab=False)

if __name__ == '__main__':
    args_len = len(sys.argv)
    if args_len < 2:
        main()
    elif args_len == 2:
        try:
            globals()[sys.argv[1]]()
        except KeyError:
            print('Error! Invalid function given as argument', file=sys.stderr)
            sys.exit(1)
    else:
        print('Error! Usage: py main.py [Function name]', file=sys.stderr)
        sys.exit(1)
    