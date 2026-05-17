'''
Write a while loop to copy the strings 'orange' of the list squares 
to the list new_squares. Stop and exit the loop if the value on the
 list is not 'orange':
 squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
'''

# declare variables
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

# i as index to access elements
i= 0
while (i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i]) # adds 'orange' to new_squares list
    i = i+1                       # i goes to 1, 2, 3, 4, 5

print(new_squares) # prints ['orange', 'orange']