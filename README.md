World Cup 2022 Stats:
A Python project that fetches live World Cup 2022 data from a public API and lets you query goal scorers, individual player stats, and the tournament's top scorer.

What It Does:
- Fetches all World Cup 2022 match data from a public JSON API
- Parses every match and extracts goal scorer information
- Stores each player's goal tally in a dictionary
- Lets you look up how many goals any player scored
- Returns the top goal scorer of the entire tournament



How to Use:
Get a specific player's goals
Uncomment the bottom of the file and call the `Goals()` function with a player's name:

print(Goals('Neymar'))       # Returns 2
print(Goals('Lionel Messi')) # Returns 7
print(Goals('Harry Kane'))   # Returns 2


If a player didn't score, it returns `0` instead of crashing.
Get the top goal scorer;

print(TopGoalScorer())
Output: Lionel Messi with 7 goals



Data Source:
All data is fetched from the open source [openfootball/worldcup.json](https://github.com/openfootball/worldcup.json) repository — no API key or sign up required.


Key Concepts Used:
- requests.get() — fetching data from a URL
- .json() — parsing the response into a Python dictionary
- for loops — iterating through matches and goals
- dict.get() — safe access with fallback to avoid crashes
- sorted() with `lambda` — sorting a dictionary by value
- Functions with error handling


Author:
Steeve Sunny 
[github.com/steeve-sunny](https://github.com/steeve-sunny)
