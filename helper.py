# Helper function to calcalute true odds of an event via assuming margin Weights are proportional to odds
def true_odds(team1, team2, draw=False):
    if not draw:
        margin = (1/team1 + 1/team2) - 1
        return {'team1': (2*team1) / (2-margin*team1), 'team2': (2*team2) / (2-margin*team2)}
    else:
        margin = (1/team1 + 1/draw + 1/team2) - 1
        return {'team1' : (3*team1) / (3 - margin*team1), 'draw': (3*draw) / (3 - margin*draw), 'team2': (3*team2) / (3 - margin*team2)}
    
# Function that converts the odds of pinnacle game dictionaries into their true odds
def convert_odds(games):
    for game in games:
        if 'draw' not in game:
            game['team1_odds'], game['team2_odds'] = true_odds(game['team1_odds'], game['team2_odds']).values()
        else:
            game['team1_odds'], game['draw'], game['team2_odds'] = \
            true_odds(game['team1_odds'], game['draw'], game['team2_odds']).values()

    return games