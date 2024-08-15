from match_events_data import *
import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_dir)
from match_events import match_teams, get_pos_ev

# Helper function that swaps team1 and team2
def swap_teams(game):
    game['team1'], game['team2'] = game['team2'], game['team1']
    game['team1_odds'], game['team2_odds'] = game['team2_odds'], game['team1_odds']
    return game

# Test for matching games
def test_fuzz():
    # Match football games
    assert match_teams(pin_data_football, book2_data_football) == football_fuzz_return

    # Match NRL games
    assert match_teams(pin_data_nrl, book2_data_nrl) == nrl_fuzz_return

def test_fuzz_complex():
    assert match_teams(pin_data_football_complex, book2_data_football_complex) == football_fuzz_complex_return

# Test positive ev outcomes are returned
def test_get_pos_ev_simple():
    # Test for football
    assert get_pos_ev(pin_data_football, book2_data_football) == football_ev_return
    # Test with matching teams not in corresponding labels (pinteam1 == book2team2)
    assert get_pos_ev(pin_data_football, list(map(swap_teams, book2_data_football))) == football_ev_return

    # Test for NRL
    assert get_pos_ev(pin_data_nrl, book2_data_nrl) == nrl_ev_return
    # Test with matching teams not in corresponding labels
    assert get_pos_ev(pin_data_nrl, list(map(swap_teams, book2_data_nrl))) == nrl_ev_return
