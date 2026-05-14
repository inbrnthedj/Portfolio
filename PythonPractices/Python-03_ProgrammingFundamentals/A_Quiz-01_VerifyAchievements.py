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

TASK 1: Write a Python program to check if a player Lionel Messi has more than 10 achievements.
        If the condition is true, print the player's name and achievements. 
        Otherwise, print "Player does not have more than 10 achievements." 


'''

# Since I don't have the actual data structure for the players, 
# I'll  start by creating a dictionary to represent the data and then check the condition for Lionel Messi.

# Creating a dictionary to represent the players and the number of their achievements
NAchievements = {
    "Serena Williams": 23,
    "Lionel Messi": 7,
    "Michael Phelps": 23,
    "Usain Bolt": 8,
    "Simone Biles": 7,
    "Roger Federer": 20,
    "Cristiano Ronaldo": 5,
    "Katie Ledecky": 7
}

# Checking if Lionel Messi has more than 10 achievements
if NAchievements.get("Lionel Messi", 0) > 10:
    print(f"Player: {NAchievements.get('Lionel Messi', 'Unknown')}")
else:
    print("Player does not have more than 10 achievements.")