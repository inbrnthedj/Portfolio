''' SCENARIO: INVENTORY MANAGEMENT SYSTEM
You are tasked with creating a simple inventory management system for a small retail store. 
'''
# Task-1 Create an empty dictionary
# First create an empty dictionary, where you will be storing the product details.
inventory ={}

# Task-2 Store the first product details in variables
# Product Name= Mobile phone
# Product Quantity= 5
# Product price= 20000
# Product Release Year= 2020
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

# Task-3 Add the first product details to the inventory dictionary
inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_releaseYear"]=ProductNo1_releaseYear

''' This will become:
|KEY                     | VALUE          |
|------------------------|----------------|
|ProductNo1              | Mobile Phone   |
|ProductNo1_quantity     | 5              |
|ProductNo1_price        | 20000          |
|ProductNo1_releaseYear  | 2020           |
'''

# Task-4 Store the second product details in variables
# Product Name= Laptop
# Product Quantity= 10
# Product price = 50000
# Product Release Year= 2023
ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023

# Task-5 Add the second product details to the inventory dictionary
inventory["ProductNo2"]= ProductNo2
inventory["ProductNo2_quantity"]= ProductNo2_quantity
inventory["ProductNo2_price"]= ProductNo2_price
inventory["ProductNo2_releaseYear"]=ProductNo2_releaseYear

# Task-6 Display the Products present in the inventory using print statement
print("The products present in the inventory are:")
print(inventory["ProductNo1"])
print(inventory["ProductNo2"])

# Task-7 Check if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory
print("ProductNo1_releaseYear" in inventory)    # This will return True, as "ProductNo1_releaseYear" is a key in the inventory dictionary.
print("ProductNo2_releaseYear" in inventory)    # This will return True, as "ProductNo2_releaseYear" is a key in the inventory dictionary.

# Task-8 Delete release year of both the products from the inventory
del(inventory["ProductNo1_releaseYear"])
del(inventory["ProductNo2_releaseYear"])