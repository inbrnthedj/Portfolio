
#  Here are some of the functions that can be used with lists include:

# --------------------------------------------------------------------------------------
# -------------------------------- MODIFYING LISTS -------------------------------------
# --------------------------------------------------------------------------------------

''' ------------------------------------------------------------------------------------
- append(): This function adds an item to the end of the list.
    list_name.append(element)
'''
my_list = [1, 2, 3]
print("Original list:", my_list)
my_list.append(4)
print("List after appending 4:", my_list)

''' ------------------------------------------------------------------------------------
- insert(): This function adds an item at a specified index in the list.
    list_name.insert(index, element)
'''
my_list.insert(1, 'a')
print("List after inserting 'a' at index 1:", my_list)

'''------------------------------------------------------------------------------------
- remove(): This function removes the first occurrence of a specified value from the list.
    list_name.remove(value)
'''
my_list.remove(2)
print("List after removing 2:", my_list)

''' ------------------------------------------------------------------------------------
- pop(): This function removes and returns the item at a specified index in the list. 
         If no index is specified, it removes and returns the last item in the list.
    list_name.pop(index)
'''
tens_list = [10, 20, 30, 40, 50]
print("Original tens_list:", tens_list)
tens_list.pop(2)
print("Tens list after popping element at index 2:", tens_list)
tens_list.pop()
print("Tens list after popping the last element:", tens_list)

'''------------------------------------------------------------------------------------
- copy(): This function creates a shallow copy of the list.
    new_list = list_name.copy()
'''
new_list = my_list.copy()
print("New list copied from my_list:", new_list)

'''------------------------------------------------------------------------------------
- count(): This function returns the number of occurrences of a specified value in the list.
    list_name.count(value)
'''
redundant_list = ['a', 'b', 'c', 'a', 'd', 'a']
print("The number of occurrences of 'a' in redundant_list:", redundant_list.count('a'))

'''------------------------------------------------------------------------------------
- sort(): This function sorts the items in the list in ascending order.
    list_name.sort()
'''
numbers = [3, 1, 4, 1, 5]
print("Original numbers list:", numbers)
numbers.sort()
print("Numbers list after sorting:", numbers)

'''------------------------------------------------------------------------------------
- reverse(): This function reverses the order of the items in the list.
    list_name.reverse()
'''
numbers.reverse()
print("Numbers list after reversing:", numbers)


'''------------------------------------------------------------------------------------
- index(): This function returns the index of the first occurrence of a specified value in the list.
    list_name.index(value)
'''
print("The index of 'c' in redundant_list:", redundant_list.index('c'))

'''------------------------------------------------------------------------------------
- len(): This function returns the number of items in the list.
    len(list_name)
'''
print("The length of my_list is:", len(my_list))


'''------------------------------------------------------------------------------------
- sum(): This function returns the sum of the items in the list.
    sum(list_name)
'''
print("The sum of numbers in the list is:", sum(numbers))

'''------------------------------------------------------------------------------------
- min(): This function returns the smallest item in the list.
    min(list_name)
'''
print("The minimum number in the list is:", min(numbers))

'''------------------------------------------------------------------------------------
- max(): This function returns the largest item in the list.
    max(list_name)
'''
print("The maximum number in the list is:", max(numbers))

'''------------------------------------------------------------------------------------
- list(): This function creates a list from an iterable object, such as a string or a tuple.
    list(iterable)
print("Creating a list from a string 'hello':", list('hello'))


'''


