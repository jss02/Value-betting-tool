from datetime import timedelta
from fuzzywuzzy import fuzz
from collections import deque

# Helper function to determine if odds have value
def calc_value(odds, true_odds):
    if odds > true_odds:
        return odds/true_odds - 1
    return False

# Helper function that returns false if game 2 is more than 6 minutes after game 1
def match_datetimes(game1, game2):
    return game1 + timedelta(minutes=6) - game2 > timedelta()

# Helper function that reverses given list and returns the length
def reverse_and_len(list_l):
    ret = deque()
    length = 0

    for element in list_l:
        ret.appendleft(element)
        length += 1

    return list(ret), length

# Helper function that returns 1 if game1['team1'] = game2['team1'] or 2 if game1['team1'] = game2['team2']
def get_match_key(game1, game2):
    if fuzz.token_set_ratio(game1['team1'], game2['team1']) + fuzz.token_set_ratio(game1['team2'], game2['team2']) > \
        fuzz.token_set_ratio(game1['team1'], game2['team2']) + fuzz.token_set_ratio(game1['team2'], game2['team1']):
        return 1
    return 2

# Helper function that returns the summed ratio of fuzz matching teams
def max_avg_ratio(game1, game2):
    ratio1 = fuzz.token_set_ratio(game1['team1'], game2['team1']) + fuzz.token_set_ratio(game1['team2'], game2['team2'])
    ratio2 = fuzz.token_set_ratio(game1['team1'], game2['team2']) + fuzz.token_set_ratio(game1['team2'], game2['team1'])
    return max(ratio1, ratio2)

# Herlper function that determines which game dictionary in the given list matches the best with the given game
def find_match(game, game_list):
    if not game_list:
        return False
    
    max_ratio = 0
    indx = 0
    for i, game2 in enumerate(game_list):
        ratio = max_avg_ratio(game, game2)
        if  ratio > max_ratio:
            max_ratio = ratio
            indx = i
    
    return indx

"""
match_teams(pin, book2)

Matches events in the given two lists and returns them as a list of tuples

Params:
    pin List[Dict]: List of games from pinnacle with their true odds
    book List[Dict]: List of games from another bookmaker

Returns:
    List[Tuple]: List of tuples containing the matching pairs
"""
def match_teams(pin, book2):
    ret = []
    book2, length = reverse_and_len(book2)
    last = length - 1

    for game in pin:
        potential_matches = []
        for i in range(last, -1 ,-1):
            game2 = book2[i]
            if not match_datetimes(game['datetime'], game2['datetime']):
                break
            
            potential_matches.append(game2)
        indx = find_match(game, potential_matches)
        if indx is not False:
            ret.append((game, book2.pop(last - indx)))
            last -= 1
    
    return ret

"""
get_pos_ev(pin, book2)

Finds odds from book2 that are of positive value relative to the odds given by pin List[float] and returns
them in a list with outcome name, odds, value, and link

Params:
    pin List[float]: List of true odds according to pinnacle.com bookmaker
    book2 List[float]: List of odds from another bookmaker

Returns:
    List[Dict]: list of dictionary containing information on the outcome with +EV
"""
def get_pos_ev(pin, book2):
    # Return if one of the lists are empty
    if not pin or not book2:
        return[]
    
    ret = [] # return list

    for game, game2 in match_teams(pin, book2):
        # Check value for team1 and team2 odds
        match_key = get_match_key(game, game2)
        for j in [1, 2]:
            value = calc_value(game2[f"team{match_key}_odds"], game[f"team{j}_odds"])
            
            # Add to return list if value is positive
            if value:
                ret.append({'name': game2['name'], 'outcome': game2[f"team{match_key}"], 'odds': game2[f"team{match_key}_odds"], 'value': value})
            match_key = 2 if match_key == 1 else 1 # Change match_key accordingly for bookmaker2 
        
        # Check if draw outcome is available
        if 'draw' in game:
            value = calc_value(game2["draw"], game["draw"])
            # Add to return list if value is positive
            if value:
                ret.append({'name': game2['name'], 'outcome': 'draw', 'odds': game2['draw'], 'value': value})
   
    return ret
