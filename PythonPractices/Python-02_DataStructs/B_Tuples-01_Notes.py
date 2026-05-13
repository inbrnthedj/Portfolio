# These are notes for Tuples in Python
# A tuple is a collection which is ordered and unchangeable. 
# In Python, tuples are written with round brackets, 
# unlike lists which are written with square brackets.

# Tuples can contain any type of data, and they can also contain duplicate values.
tuple1 = ("disco",10,1.2 ) # This is a tuple with three elements: a string, an integer, and a float.
print("A tuple can contain any type of data like this:")
print(tuple1)

# Tuples are ordered, which means that the items have a defined order, and that order will not change.
print("The first item in the tuple is:")
print(tuple1[0])

# We can print out the type of the tuple to confirm that it is indeed a tuple:
print("The type of tuple1 is:")
print(type(tuple1))

# We can also print out the length of the tuple to see how many items it contains:
print("The length of tuple1 is:")
print(len(tuple1))

# We can also print out the type of each value in the tuple:
print("The type of each value in the tuple is:")
print(type(tuple1[0]), type(tuple1[1]), type(tuple1[2]))

# We can use negative indexing to access the items in the tuple. 
# Negative indexing means that we start counting from the end of 
# the tuple, with -1 being the last item, -2 being the second to last item, and so on.
print("The last item in the tuple is also indexed as -1:")
print(tuple1[-1])

# CONCATENATION OF TUPLES
# To concatenate two tuples, we can use the + operator.
tuple2 = ("hard rock", 10)
print("tuple1 is: ", tuple1)
print("tuple2 is: ", tuple2)
print("Concatenating tuple1 and tuple2 gives:")
print(tuple1 + tuple2)

# SLICING OF TUPLES
# We can slice tuples just like we can slice lists. 
# Slicing means that we can access a range of items in the tuple.
print("The first two items in the tuple are:")
print(tuple1[0:2])

# SORTING OF TUPLES
# We cannot sort a tuple because tuples are immutable, which means that 
# we cannot change the items in the tuple after it has been created.
# However, we can sort a tuple by converting it to a list, sorting the list, and then converting it back to a tuple.
tuple3 = (3, 1, 2)
print("tuple3 is: ", tuple3)
sorted_tuple3 = tuple(sorted(tuple3))
print("Sorting tuple3  with the use of sorted() gives:")
print(sorted_tuple3)

# NESTED TUPLES
# We can also have tuples within tuples, which are called nested tuples.
nested_tuple = (1, 2, (3, 4), 5)
print("nested_tuple is: ", nested_tuple)
print("The nested tuple contains another tuple: ", nested_tuple[2])

# TUPLE INDEXING
# We can also access the items in the nested tuple by using multiple indexing.
print("The first item in the nested tuple is: ", nested_tuple[2][0])
print("The second item in the nested tuple is: ", nested_tuple[2][1])

# TUPLE UNPACKING
# We can also unpack a tuple into individual variables.
tuple4 = ("rock", "pop", "jazz")
print("tuple4 is: ", tuple4)
genre1, genre2, genre3 = tuple4
print("Unpacking tuple4 gives:")
print(genre1, genre2, genre3)
