#Here are some of the functions that can be used with tuples:

''' ------------------------------------------------------------------------------------
- count(): used to count how many times a specified element appears in the tuple.
    SYNTAX: tuple_name.count(element)
'''
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple")) #Counts the number of times apple is found in tuple.
#Output: 2

''' ------------------------------------------------------------------------------------
- index(): used to find the first occurrence of a specified value and returns its index.
    If the value is not found, it raises a ValueError.
    SYNTAX: tuple_name.index(value)
'''
#Returns the index of the first occurrence of banana in tuple
print(fruits.index("banana")) 
#Output: 1
''

''' ------------------------------------------------------------------------------------
- sum(): This function returns the sum of all the items in the tuple, provided that
    all the items are numeric (int or float).
        SYNTAX: sum(tuple_name)
'''
numbers = (10, 20, 5, 30)
print(sum(numbers))
#Output: 65

''' ------------------------------------------------------------------------------------
- min(): This function returns the smallest item in the tuple.
    SYNTAX: min(tuple_name)
- max(): This function returns the largest item in the tuple.
    SYNTAX: max(tuple_name)
'''
numbers = (10, 20, 5, 30)
print(min(numbers))  
#Output: 5
print(max(numbers))
#Output: 30

''' ------------------------------------------------------------------------------------
- len(): This function returns the number of items in the tuple.
    SYNTAX: len(tuple_name)
'''
fruits = ("apple", "banana", "orange")
print(len(fruits)) #Returns length of the tuple.
#Output: 3

