# Value Betting Software
![Python](https://img.shields.io/badge/python-3.10-blue) ![Release](https://img.shields.io/badge/version-v1.0-clairvoyant)
<p align='center'><a href='https://www.pinnacle.com/en/' target='_blank'><img width='150' height='80' src="https://logowik.com/content/uploads/images/pinnacle2317.logowik.com.webp"></a><a href='https://www.sportsbet.com.au/' target='_blank'><img width='150' height='80' src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Sportsbet_Logo.jpg"></a><a href='https://www.tab.com.au/' target='_blank'><img width='150' height='80' src="https://logovectorseek.com/wp-content/uploads/2020/04/tab-com-au-logo-vector.png"></a></p>

## Description
Python program that identifies bookmaker pricings with positive expected value. Uses Pinnacle's odds to calculate the true odds of events.

Based on <a href='https://www.football-data.co.uk/The_Wisdom_of_the_Crowd_updated.pdf' target='_blank'>Wisdom of the Crowd</a> by <a href='https://www.football-data.co.uk/' target='_blank'>football-data.co.uk</a>.
- More concise web article <a href='https://www.football-data.co.uk/blog/wisdom_of_the_crowd.php' target='_blank'>here</a>.

### Value betting
Value betting is betting on outcomes that have a higher probability to occur than implied by the available odds, resulting in positive expected value.
<p align="center"><a href="https://www.techopedia.com/gambling-guides/value-betting" target='_blank'><img width=80% src='https://www.techopedia.com/wp-content/uploads/2023/05/Value-betting-explained.jpg'></a></p>

## Installation
1. Clone the repository
```
git clone
```
2. Change to project directory
```
cd Value-betting-software
```
3. Install dependencies (virtual env recommended)
```
pip install -r requirements.txt
```

## Usage
##### Note: including Tab will open a new chrome window for every link due to headless mode being disabled by the website
To get results from all bookmakers:
```
py src/main.py
```
To get results from bookmakers excluding tab:
```
py src/main.py not_tab
```
- Note: `py` is interchangeable with `python` or `python3`

### Adding or removing links
To add a link:
1. Get links for the league of the sport you want to add
	- Must be the URL displaying the odds for the events of the whole league
		- Example page screenshots: Pinnacle Tab Sportsbet
2. Add to links dictionary in `link_manager.py` in the format:
```Python3
'<league_name>': {'pin': '<link for pinnacle>', 'sb': '<link for sportsbet>', 'tab': '<link for tab>'}
```
	- Note: make sure a comma is present before and after the new entry to maintain valid dictionary format

To remove a link, simply remove the key value entry for the league you want to remove from the links dictionary in `link_manager.py`.

