'''IndexError'''
# accessing an element in a list outside the valid index range
my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError