from datetime import timedelta
from fuzzywuzzy import fuzz

# Helper function to determine if odds have value
def calc_value(odds, true_odds):
    if odds > true_odds:
        return odds/true_odds - 1
    return False

# Helper function that returns false if game 2 is more than 10 minutes after game 1
def match_datetimes(game1, game2):
    return game1 + timedelta(minutes=10) - game2 > timedelta()

# Function that checks both teams are the same in both games
# Returns 1 if team1 key in both dict are the same teams, 2 otherwise
def match_teams(game1, game2):
    if (fuzz.token_set_ratio(game1['team1'], game2['team1']) > 90 and
        fuzz.token_set_ratio(game1['team2'], game2['team2']) > 90):
        return 1
    if (fuzz.token_set_ratio(game1['team1'], game2['team2']) > 90 and
        fuzz.token_set_ratio(game1['team2'], game2['team1']) > 90):
        return 2

    return False
    
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

    # Reverse book2 list as popping is more efficient than remove method
    book2.reverse()
    last = len(book2) - 1 # Keep track of last index

    # Iterate through list of pinnacle games and try to match with other bookmaker events
    for game in pin:
        # Iterate in reverse order
        for i in range(last, -1, -1):
            game2 = book2[i]

            # Stop iterating if the game2 is more than 10 minutes after game1 since the list iterates to later events
            if not match_datetimes(game['datetime'], game2['datetime']):
                break
            
            # Check if teams match in both games
            match_key = match_teams(game, game2)
            if match_key:
                # Check value for team1 and team2 odds
                for i in [1, 2]:
                    value = calc_value(game2[f"team{match_key}_odds"], game[f"team{i}_odds"])
                    match_key = 2 if match_key == 1 else 1 # Change match_key accordingly for bookmaker2 
                    
                    # Add to return list if value is positive
                    if value:
                        ret.append({'name': game2['name'], 'outcome': game[f"team{i}"], 'odds': game2[f"team{match_key}_odds"], 'value': value})
                
                # Check if draw outcome is available
                if 'draw' in game:
                    value = calc_value(game2["draw"], game["draw"]) 

                    # Add to return list if value is positive
                    if value:
                        ret.append({'name': game2['name'], 'outcome': 'draw', 'odds': game2['draw'], 'value': value})

                # Remove event from bookmaker2 list
                book2.pop(i)
                last -= 1

                # Event is matched so break to next pinnacle event
                break
    
    return ret
