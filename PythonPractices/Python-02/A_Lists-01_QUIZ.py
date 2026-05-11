# This is a series of quiz in IBM's course for Python. The quiz is about lists.

# SOME NOTES:
# - In a Jupyter cell, plainly writing the variable name will print the value of the variable. 
# - In a Python script, you need to use the print() function to display the value of a variable.

# 1 - Create a list a_list with the following elements: 1, hello, [1,2,3] and True.
a_list = [1, 'hello', [1, 2, 3], True]
print("a_list has the following elements:")
print(a_list)

# 2 - Find the value stored at index 1 of a_list.
print("the value stored at index 1 of a_list is:")
print(a_list[1])

# 3 - Retrieve the elements stored at index 1, 2 and 3 of a_list.
print("the elements stored at index 1, 2 and 3 of a_list are:")
print(a_list[1:4])  # This will retrieve elements from index 1 to 3 (4 is exclusive)

# 4 - Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a']
B = [2, 1, 'd']
print("Concatenating lists A and B gives:")
print(A + B)