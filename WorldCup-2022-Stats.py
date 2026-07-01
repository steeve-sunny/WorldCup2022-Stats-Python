import requests

response = requests.get("https://raw.githubusercontent.com/openfootball/worldcup.json/master/2022/worldcup.json")
info = response.json()

goal_scorers = {}

for match in info['matches']:
     # extracting the name from the goal object inside match 
     for goal in match.get("goals1", []): # add the empty list for error handling
        name = goal["name"]

        # need to store goal scorer name and amount of goals somewhwre
        # DO it by storing it in our goal_scorers dictionary
        if name not in goal_scorers:
            goal_scorers[name] = 1
        else:
            goal_scorers[name] += 1
     
     # we apply the same approach and logic for goals2 section
     for goal in match.get("goals2", []):
        name = goal["name"]

        if name not in goal_scorers:
            goal_scorers[name] = 1
        else:
            goal_scorers[name] += 1


# we need to define a function to get the amount of goals scored by a certain person
# how the function works by is that you need to insert a players name and the amount of goals will appear
# if a person hasn't scored we need to handle the key error.

def Goals(name):
    if name in goal_scorers:
        return goal_scorers[name]
    else:
        return 0

# we need to sort the goal scorer dictionary and get a top goalscorer of the tournament
# we will sort the dictionary inside of the function

def TopGoalScorer():
    sorted_scorers = sorted(goal_scorers.items(), key=lambda x: x[1], reverse=True)
    return f"{sorted_scorers[0][0]} with {sorted_scorers[0][1]} goals "

#when wanting to use the particular functions need to uncomment the code below
#you have to type in the player name for the Goals function

#print(TopGoalScorer())
#print(Goals('Neymar'))
