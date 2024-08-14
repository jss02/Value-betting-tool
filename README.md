# Value Betting Software
![Python](https://img.shields.io/badge/python-3.10-blue) ![Release](https://img.shields.io/badge/version-v1.0-clairvoyant) [![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://github.com/jss02/Value-betting-software/blob/src/LICENSE.txt)
<p align='center'><a href='https://www.pinnacle.com/en/'><img width='150' height='80' src="https://logowik.com/content/uploads/images/pinnacle2317.logowik.com.webp"></a><a href='https://www.sportsbet.com.au/' ><img width='150' height='80' src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Sportsbet_Logo.jpg"></a><a href='https://www.tab.com.au/' ><img width='150' height='80' src="https://logovectorseek.com/wp-content/uploads/2020/04/tab-com-au-logo-vector.png"></a></p>

## Description
Python program that identifies bookmaker pricings with positive expected value. Uses Pinnacle's odds to calculate the true odds of events.

Based on <a href='https://www.football-data.co.uk/The_Wisdom_of_the_Crowd_updated.pdf' >Wisdom of the Crowd</a> by <a href='https://www.football-data.co.uk/' >football-data.co.uk</a>.
- More concise web article <a href='https://www.football-data.co.uk/blog/wisdom_of_the_crowd.php' >here</a>.

### Value betting
Value betting is betting on outcomes that have a higher probability to occur than implied by the available odds, resulting in positive expected value.
<p align="center"><a href="https://www.techopedia.com/gambling-guides/value-betting" ><img width=80% src='https://www.techopedia.com/wp-content/uploads/2023/05/Value-betting-explained.jpg'></a></p>

### Removing the margin to get the true odds
The margin from Pinnacle's odds are removed using the Margin Proportional to the Odds formula:

$odds_{true}=\frac{n\*odds_{pinnacle}}{n-M\*odds_{pinnacle}}$

Where:
- $odds_{true}$: true odds of an outcome
- $n$: number of outcomes
- $M$: margin

The margin is given by:

$M=\frac{1}{odds_{1}} + \frac{1}{odds_{2}} + ... - 1 = \sum_{i=1}^n \frac{1}{odds_{i}}$  - 1

Where:
- $M$: margin
- $n$: number of outcomes

### Margin Proportional to the Odds
Margin Proportional to the Odds was chosen as it was the simplest of the two models that best yielded the true odds based on the data.
<p align='center'><img width=60% src='assets/margin_returns.JPG'></p>
- Table represents the yield from bets with 0 expected value based on the margin models

\
It also yielded profits slightly above the expected yield when used as the model to calculate true odds.
<p align='center'><img src='assets/margin_prop_returns.JPG'></p>

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
#### Note: including Tab will open a new chrome window for every link due to headless mode being disabled by the website
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
		- Examples: <a href='assets/pin.png' >Pinnacle</a> <a href='assets/tab.png' >Tab</a> <a href='assets/sb.png' >Sportsbet</a>
2. Add to links dictionary in `link_manager.py` in the format:
```Python3
'<league_name>': {'pin': '<link for pinnacle>', 'sb': '<link for sportsbet>', 'tab': '<link for tab>'}
```
- Note: make sure a comma is present before and after the new entry to maintain valid dictionary format

To remove a link, simply remove the key value entry for the league you want to remove from the links dictionary in `link_manager.py`.

## Credits/Acknowledgments
Theory based on <a href='https://www.football-data.co.uk/The_Wisdom_of_the_Crowd_updated.pdf' >Wisdom of the Crowd</a> by <a href='https://www.football-data.co.uk/' >football-data.co.uk</a>. Visit the <a href='https://www.football-data.co.uk/blog/wisdom_of_the_crowd.php' >website article</a>.

## Potential improvements
### Multithreading
Multithreading would make the program faster as we could scrape multiple websites at once. Opening the webdriver sequentially wastes a lot of time at I/O waiting for as chromedriver which is slow to load the websites.

### Using betfair odds to calculate true odds
Pinnacle delays odds by 15 minutes for users that are not logged in. Using Betfair exchange odds through their API (costs £299) would improve the accuracy of the results.

### Adding more markets
More markets such as the line, handicaps, and player props would increase the volume of bets available and thus increase the return. However, the data in the theory only includes football 1x2 bets.

### More bookmakers
Adding more bookmakers would also increase the volume of bets available.