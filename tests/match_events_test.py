from match_events_data import *
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from match_events import match_teams, get_pos_ev

# Helper function that swaps team1 and team2
def swap_teams(game):
    game['team1'], game['team2'] = game['team2'], game['team1']
    game['team1_odds'], game['team2_odds'] = game['team2_odds'], game['team1_odds']
    return game

# Test for matching games
def test_fuzz():
    # Match football games
    assert match_teams(pin_data_football[0], book2_data_football[0])
    assert match_teams(pin_data_football[1], book2_data_football[1])
    assert match_teams(pin_data_football[2], book2_data_football[2])
    assert match_teams(pin_data_football[3], book2_data_football[3])

    # Match NRL games
    assert match_teams(pin_data_nrl[0], book2_data_nrl[0])
    assert match_teams(pin_data_nrl[1], book2_data_nrl[1])
    assert match_teams(pin_data_nrl[2], book2_data_nrl[2])
    assert match_teams(pin_data_nrl[3], book2_data_nrl[3])

# Test positive ev outcomes are returned
def test_get_pos_ev_simple():
    # Test for football
    assert get_pos_ev(pin_data_football, book2_data_football) == football_return
    # Test with matching teams not in corresponding labels (pinteam1 == book2team2)
    assert get_pos_ev(pin_data_football, list(map(swap_teams, book2_data_football))) == football_return

    # Test for NRL
    assert get_pos_ev(pin_data_nrl, book2_data_nrl) == nrl_return
    # Test with matching teams not in corresponding labels
    assert get_pos_ev(pin_data_nrl, list(map(swap_teams, book2_data_nrl))) == nrl_return
