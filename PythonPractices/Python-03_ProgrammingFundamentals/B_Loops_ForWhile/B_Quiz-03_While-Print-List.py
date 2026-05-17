''' 
Write a while loop to display the values of the Rating of an 
album playlist stored in thePlayListRatings list. 
If the score is less than 6, exit the loop. 
The list PlayListRatings is given by: 
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
'''

# declare list
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i as index to access elements
i =0
# Rating to print
Rating = PlayListRatings[0]

# i will go from 0 to the length of list
# Rating as criterion to stop the loop when it is less than 6
while (i < len(PlayListRatings) and Rating >= 6):
    print(Rating)               # prints from 10
    i = i+1                     # i goes to 1, 2, 3, 4, 5
    Rating = PlayListRatings[i] # substitutes to next element
    i=i+1                       # sets new i for next loop iteration