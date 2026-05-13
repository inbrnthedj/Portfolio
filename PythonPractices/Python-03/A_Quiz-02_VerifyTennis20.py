''' Here's the data for the quiz:

| Player Name       | Sport     | Achievements              |
|-------------------|-----------|---------------------------|
| Serena Williams   | Tennis    | 23 Grand Slam titles      |
| Lionel Messi      | Football  | 7 Ballon d'Or awards      |
| Michael Phelps    | Swimming  | 23 Olympic gold medals    |
| Usain Bolt        | Athletics | 8 Olympic gold medals     |
| Simone Biles      | Gymnastics| 7 Olympic medals (4 gold) |
| Roger Federer     | Tennis    | 20 Grand Slam titles      |
| Cristiano Ronaldo | Football  | 5 Ballon d'Or awards      |
| Katie Ledecky     | Swimming  | 7 Olympic gold medals     |

TASK 2: Write a Python program to check if a player belongs to the sport Tennis or 
has exactly 20 achievements. If the condition is true, print a success message.
'''

# Since I don't have the actual data structure for the players, 
# I'll  start by creating a dictionary to represent the data and then check the condition for Lionel Messi.

# Creating a dictionary to represent the players and their sports
playerSport = {
    "Serena Williams": "Tennis",
    "Lionel Messi": "Football",
    "Michael Phelps": "Swimming",
    "Usain Bolt": "Athletics",
    "Simone Biles": "Gymnastics",
    "Roger Federer": "Tennis",
    "Cristiano Ronaldo": "Football",
    "Katie Ledecky": "Swimming"
}

# Creating a dictionary to represent the players and the number of their achievements
playerAchievements = {
    "Serena Williams": 23,
    "Lionel Messi": 7,
    "Michael Phelps": 23,
    "Usain Bolt": 8,
    "Simone Biles": 7,
    "Roger Federer": 20,
    "Cristiano Ronaldo": 5,
    "Katie Ledecky": 7
}

# Now that I have my data structures, I can check the condition for each player and print a success message if the condition is true.
# I am going to use logical operators to check if a player belongs to the sport Tennis or has exactly 20 achievements.

# Checking the condition for each player
for player in playerSport:
    if playerSport[player] == "Tennis" or playerAchievements[player] == 20:
        print(f"{player} meets the criteria!")
        print(f" {player} plays {playerSport[player]} and has {playerAchievements[player]} achievements, making them a successful player!")
    else:
        print(f"{player} does not meet the criteria.")