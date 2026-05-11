#This is a scenario-based practice for lists in Python.
'''
SCENARIO: SHOPPING LIST

TASK 1: Create an empty List
TASK 2: Now store the number of items to the shopping_list
    - Watch
    - Laptop
    - Shoes
    - Pen
    - Clothes
TASK 3: Add a new item to the shopping_list
    Seems like I missed one item "Football" to add in the shopping list.
TASK 4: Print the first item from the shopping_list
TASK 5: Print the last item from the shopping_list
    Let's check the last time that we need to buy.
Task-6 Print the entire Shopping List
Task-7 Print the item that are important to buy from the Shopping List
    Print "Laptop" and "shoes"
Task-8 Change the item from the shopping_list
    Instead of "Pen" I want to buy "Notebook" let's change the item stored in the list.
Task-9 Delete the item from the shopping_list that is not required
    Let's delete items that are unimportant, such as; I don't want to buy Clothes, let's delete it.
Task-10 Print the shopping list
We are ready with our shopping list.
'''

# Task 1: Create an empty List
shopping_list = []

# Task 2: Now store the number of items to the shopping_list
shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]

# Task 3: Add a new item to the shopping_list
shopping_list.append("Football")

# Task 4: Print the first item from the shopping_list
print("The first item from the shopping_list is:")
print(shopping_list[0])

# Task 5: Print the last item from the shopping_list
print("The last item from the shopping_list is:")
print(shopping_list[-1])

# Task-6 Print the entire Shopping List
print("The entire shopping list is:")
print(shopping_list)

# Task-7 Print the item that are important to buy from the Shopping List
print("The important items to buy from the shopping list are:")
print(shopping_list[1], shopping_list[2])  # "Laptop" and "Shoes"

# Task-8 Change the item from the shopping_list
shopping_list[3] = "Notebook"  # Changing "Pen" to "Notebook"
print("The updated shopping list is:")
print(shopping_list)

# Task-9 Delete the item from the shopping_list that is not required
shopping_list.remove("Clothes")  # Removing "Clothes" from the list
print("The shopping list after removing Clothes is:")
print(shopping_list)

# Task-10 Print the shopping list
print("The final shopping list is:")
print(shopping_list)
