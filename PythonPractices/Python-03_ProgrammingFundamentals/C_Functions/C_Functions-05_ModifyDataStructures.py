'''
How to Modify Data Structures in Functions
- Functions can change data structures like lists and dictionaries
- When you pass a data structure to a function, it can be modified
- This is because data structures are mutable (can be changed)
'''

# 1 - Initialize an empty list
my_list = []

# 2 - Define a function to add an item to the list
def add_item(data_structure, item):
    '''This function adds an item to the provided data structure.
    data_structure: The list to which the item will be added
    item: The item to be added to the list
    '''
    data_structure.append(item) # Modify the list by adding a new item

# 3 - Define a function to remove elements
def remove_item(data_structure, item):
    '''This function verifies if the item is inside the list and then
    removes it if present. Otherwise, it informs user that the item
    does not belong in the list'''
    if item in data_structure:
        data_structure.remove(item)
    else:
        print(f"{item} not found in the list.")
    

# 4 - add items to the list

add_item(my_list,17)
add_item(my_list, 100)

# 5 - Print current list
print("Current list:", my_list)

# 6 - Remove item from the list
remove_item(my_list,17)
remove_item(my_list,"letter")   # This will print text saying that "letter" is not in the list

# 7 - Print new list
print("New List:", my_list)