# This is a series of quiz in IBM's course for Python. The quiz is about tuples.

'''
Here are some of the functions that can be used with tuples include:
- index(): This function returns the index of the first occurrence of a specified value in the tuple.
- sorted(): This function returns a sorted list of the items in the tuple.
- len(): This function returns the number of items in the tuple.
'''

# sample tuple - These are tuples to be used in the quiz

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

# 1 - Find the length of the tuple, genres_tuple.
print("The length of genres_tuple is:")
print(len(genres_tuple)) # This returns 8.

# 2 - Access the element, with respect to index 3
print("The element at index 3 of genres_tuple is:")
print(genres_tuple[3]) # This returns 'hard rock'.

# 3 - Use slicing to obtain indexes 3, 4 and 5:
print("The elements at index 3, 4 and 5 of genres_tuple are:")
print(genres_tuple[3:6]) # This returns ('hard rock', 'soft rock', 'R&B').

# 4 - Find the first two elements of the tuple genres_tuple:
print("The first two elements of genres_tuple are:")
print(genres_tuple[0:2]) # This returns ('pop', 'rock').

# 5 - Find the index of 's' in "disco":
print("The index of 's' in 'disco' is:")
print("disco".index("s")) # This returns 1.
print(genres_tuple[7].index("s")) # This also returns 1, since 'disco' is at index 7 in genres_tuple.

# 6 - Generate a sorted List from the Tuple C_tuple=(-5, 1, -3)
C_tuple = (-5, 1, -3)
print("The sorted list generated from C_tuple is:")
print(sorted(C_tuple)) # This returns [-5, -3, 1].