import datetime

# Test data for pinnacle football games
pin_data_football = [
    {'team1': 'Manchester United', 'team2': 'Fulham',
     'datetime': datetime.datetime(2024, 8, 17, 5, 0),
     'team1_odds': 1.49, 'draw': 4.47, 'team2_odds': 5.57},
    {'team1': 'Ipswich Town', 'team2': 'Liverpool',
     'datetime': datetime.datetime(2024, 8, 17, 21, 30),
     'team1_odds': 7.24, 'draw': 5.21, 'team2_odds': 1.34},
    {'team1': 'Nottingham Forest', 'team2': 'Bournemouth',
     'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 2.54, 'draw': 3.38, 'team2_odds': 2.66},
    {'team1': 'Arsenal', 'team2': 'Wolves',
     'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 1.174, 'draw': 7.06, 'team2_odds': 11.68}
]

# Test data for alternate bookmaker football games
book2_data_football = [
    {'name': 'Man United v Fulham', 'team1': 'Man United',
     'team2': 'Fulham', 'datetime': datetime.datetime(2024, 8, 17, 5, 0),
     'team1_odds': 1.5, 'draw': 4.5, 'team2_odds': 5.5},
    {'name': 'Ipswich v Liverpool', 'team1': 'Ipswich',
     'team2': 'Liverpool', 'datetime': datetime.datetime(2024, 8, 17, 21, 30),
     'team1_odds': 8.0, 'draw': 5.0, 'team2_odds': 1.35},
     {'name': 'Nottinghm Forest v Bournemouth', 'team1': 'Nottinghm Forest',
      'team2': 'Bournemouth', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
      'team1_odds': 2.5, 'draw': 3.4, 'team2_odds': 2.6},
    {'name': 'Arsenal v Wolverhampton', 'team1': 'Arsenal',
     'team2': 'Wolverhampton', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 1.2, 'draw': 6.5, 'team2_odds': 13.0}
]

football_fuzz_return = [
    ({'team1': 'Manchester United', 'team2': 'Fulham', 'datetime': datetime.datetime(2024, 8, 17, 5, 0),
      'team1_odds': 1.49, 'draw': 4.47, 'team2_odds': 5.57},
      {'name': 'Man United v Fulham', 'team1': 'Man United', 'team2': 'Fulham',
       'datetime': datetime.datetime(2024, 8, 17, 5, 0), 'team1_odds': 1.5, 'draw': 4.5, 'team2_odds': 5.5}),
    ({'team1': 'Ipswich Town', 'team2': 'Liverpool', 'datetime': datetime.datetime(2024, 8, 17, 21, 30),
      'team1_odds': 7.24, 'draw': 5.21, 'team2_odds': 1.34},
      {'name': 'Ipswich v Liverpool', 'team1': 'Ipswich', 'team2': 'Liverpool',
       'datetime': datetime.datetime(2024, 8, 17, 21, 30), 'team1_odds': 8.0, 'draw': 5.0, 'team2_odds': 1.35}),
    ({'team1': 'Nottingham Forest', 'team2': 'Bournemouth', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
      'team1_odds': 2.54, 'draw': 3.38, 'team2_odds': 2.66},
      {'name': 'Nottinghm Forest v Bournemouth', 'team1': 'Nottinghm Forest', 'team2': 'Bournemouth',
       'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'team1_odds': 2.5, 'draw': 3.4, 'team2_odds': 2.6}),
    ({'team1': 'Arsenal', 'team2': 'Wolves', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
      'team1_odds': 1.174, 'draw': 7.06, 'team2_odds': 11.68},
      {'name': 'Arsenal v Wolverhampton','team1': 'Arsenal', 'team2': 'Wolverhampton',
       'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'team1_odds': 1.2, 'draw': 6.5, 'team2_odds': 13.0})
]

football_ev_return = [
    {'name': 'Man United v Fulham', 'outcome': 'Man United', 'odds': 1.5, 'value': 0.006711409395973256},
    {'name': 'Man United v Fulham', 'outcome': 'draw', 'odds': 4.5, 'value': 0.006711409395973256},
    {'name': 'Ipswich v Liverpool', 'outcome': 'Ipswich', 'odds': 8.0, 'value': 0.1049723756906078},
    {'name': 'Ipswich v Liverpool', 'outcome': 'Liverpool', 'odds': 1.35, 'value': 0.00746268656716409},
    {'name': 'Nottinghm Forest v Bournemouth', 'outcome': 'draw', 'odds': 3.4, 'value': 0.00591715976331364},
    {'name': 'Arsenal v Wolverhampton', 'outcome': 'Arsenal', 'odds': 1.2, 'value': 0.022146507666098936},
    {'name': 'Arsenal v Wolverhampton', 'outcome': 'Wolverhampton', 'odds': 13.0, 'value': 0.1130136986301371}
]

# Test data for pinnacle NRL games
pin_data_nrl = [
    {'team1': 'South Sydney Rabbitohs', 'team2': 'Melbourne Storm',
     'datetime': datetime.datetime(2024, 8, 8, 19, 50), 'team1_odds': 4.54, 'team2_odds': 1.185},
    {'team1': 'Gold Coast Titans', 'team2': 'Cronulla Sharks',
     'datetime': datetime.datetime(2024, 8, 9, 18, 0), 'team1_odds': 1.564, 'team2_odds': 2.43},
    {'team1': 'Parramatta Eels', 'team2': 'Penrith Panthers',
     'datetime': datetime.datetime(2024, 8, 9, 20, 0), 'team1_odds': 4.67, 'team2_odds': 1.177},
    {'team1': 'Canberra Raiders', 'team2': 'Manly Sea Eagles',
     'datetime': datetime.datetime(2024, 8, 10, 15, 0), 'team1_odds': 2.23, 'team2_odds': 1.666}
]

# Test data for alternate bookmaker NRL games
book2_data_nrl = [
    {'name': 'South v Melbourne', 'team1': 'Souths', 'team2': 'Melbourne',
     'datetime': datetime.datetime(2024, 8, 8, 19, 50), 'team1_odds': 5.5,
     'team2_odds': 1.15},
    {'name': 'Gold Coast v Cronulla', 'team1': 'Gold Coast', 'team2': 'Cronulla',
     'datetime': datetime.datetime(2024, 8, 9, 18, 0), 'team1_odds': 1.55,
     'team2_odds': 2.45},
    {'name': 'Parramatta v Penrith', 'team1': 'Parramatta', 'team2': 'Penrith',
     'datetime': datetime.datetime(2024, 8, 9, 20, 0), 'team1_odds': 6.0, 'team2_odds': 1.13},
    {'name': 'Canberra v Manly', 'team1': 'Canberra', 'team2': 'Manly',
     'datetime': datetime.datetime(2024, 8, 10, 15, 0), 'team1_odds': 2.3, 'team2_odds': 1.62}
]

nrl_fuzz_return = [
    ({'team1': 'South Sydney Rabbitohs', 'team2': 'Melbourne Storm',
      'datetime': datetime.datetime(2024, 8, 8, 19, 50), 'team1_odds': 4.54, 'team2_odds': 1.185},
      {'name': 'South v Melbourne', 'team1': 'Souths', 'team2': 'Melbourne',
       'datetime': datetime.datetime(2024, 8, 8, 19, 50), 'team1_odds': 5.5, 'team2_odds': 1.15}),
    ({'team1': 'Gold Coast Titans', 'team2': 'Cronulla Sharks',
      'datetime': datetime.datetime(2024, 8, 9, 18, 0), 'team1_odds': 1.564, 'team2_odds': 2.43},
      {'name': 'Gold Coast v Cronulla', 'team1': 'Gold Coast', 'team2': 'Cronulla',
       'datetime': datetime.datetime(2024, 8, 9, 18, 0), 'team1_odds': 1.55, 'team2_odds': 2.45}),
    ({'team1': 'Parramatta Eels', 'team2': 'Penrith Panthers',
      'datetime': datetime.datetime(2024, 8, 9, 20, 0), 'team1_odds': 4.67, 'team2_odds': 1.177},
      {'name': 'Parramatta v Penrith', 'team1': 'Parramatta', 'team2': 'Penrith',
       'datetime': datetime.datetime(2024, 8, 9, 20, 0), 'team1_odds': 6.0, 'team2_odds': 1.13}),
    ({'team1': 'Canberra Raiders', 'team2': 'Manly Sea Eagles',
      'datetime': datetime.datetime(2024, 8, 10, 15, 0), 'team1_odds': 2.23, 'team2_odds': 1.666},
      {'name': 'Canberra v Manly', 'team1': 'Canberra', 'team2': 'Manly',
       'datetime': datetime.datetime(2024, 8, 10, 15, 0), 'team1_odds': 2.3, 'team2_odds': 1.62})
]

nrl_ev_return = [
    {'name': 'South v Melbourne', 'outcome': 'Souths', 'odds': 5.5, 'value': 0.21145374449339216},
    {'name': 'Gold Coast v Cronulla', 'outcome': 'Cronulla', 'odds': 2.45, 'value': 0.008230452674897082},
    {'name': 'Parramatta v Penrith', 'outcome': 'Parramatta', 'odds': 6.0, 'value': 0.2847965738758029},
    {'name': 'Canberra v Manly', 'outcome': 'Canberra', 'odds': 2.3, 'value': 0.03139013452914785}
]

pin_data_football_complex = [
    {'team1': 'Newcastle United', 'team2': 'Southampton', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 1.318, 'draw': 5.37, 'team2_odds': 7.61},
    {'team1': 'Everton','team2': 'Brighton and Hove Albion', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 2.45, 'draw': 3.28, 'team2_odds': 2.83},
    {'team1': 'Nottingham Forest','team2': 'Bournemouth', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 2.54, 'draw': 3.38, 'team2_odds': 2.66},
    {'team1': 'Arsenal', 'team2': 'Wolves', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
     'team1_odds': 1.174, 'draw': 7.06, 'team2_odds': 11.68}
]

book2_data_football_complex = [
    {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Newcastle v Southampton', 'team1': 'Newcastle',
     'team1_odds': 1.33, 'team2': 'Southampton', 'team2_odds': 8.5, 'draw': 5.5},
    {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Nottm Forest v Bournemouth', 'team1': 'Nottm Forest',
     'team1_odds': 2.5, 'team2': 'Bournemouth', 'team2_odds': 2.7, 'draw': 3.5},
    {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Everton v Brighton', 'team1': 'Everton',
     'team1_odds': 2.5, 'team2': 'Brighton', 'team2_odds': 2.8, 'draw': 3.3},
    {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Arsenal v Wolves', 'team1': 'Arsenal',
    'team1_odds': 1.18, 'team2': 'Wolves', 'team2_odds': 14.0, 'draw': 7.0}
]

football_fuzz_complex_return = [
    ({'team1': 'Newcastle United', 'team2': 'Southampton', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
      'team1_odds': 1.318, 'draw': 5.37, 'team2_odds': 7.61},
      {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Newcastle v Southampton', 'team1': 'Newcastle',
       'team1_odds': 1.33, 'team2': 'Southampton', 'team2_odds': 8.5, 'draw': 5.5}),
    ({'team1': 'Everton', 'team2': 'Brighton and Hove Albion', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
      'team1_odds': 2.45, 'draw': 3.28, 'team2_odds': 2.83},
      {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Everton v Brighton', 'team1': 'Everton',
       'team1_odds': 2.5, 'team2': 'Brighton', 'team2_odds': 2.8, 'draw': 3.3}),
    ({'team1': 'Nottingham Forest', 'team2': 'Bournemouth', 'datetime': datetime.datetime(2024, 8, 18, 0, 0),
      'team1_odds': 2.54, 'draw': 3.38, 'team2_odds': 2.66},
      {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Nottm Forest v Bournemouth',
       'team1': 'Nottm Forest', 'team1_odds': 2.5, 'team2': 'Bournemouth', 'team2_odds': 2.7, 'draw': 3.5}),
    ({'team1': 'Arsenal', 'team2': 'Wolves', 'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'team1_odds': 1.174,
      'draw': 7.06, 'team2_odds': 11.68},
      {'datetime': datetime.datetime(2024, 8, 18, 0, 0), 'name': 'Arsenal v Wolves', 'team1': 'Arsenal',
       'team1_odds': 1.18, 'team2': 'Wolves', 'team2_odds': 14.0, 'draw': 7.0})
]
