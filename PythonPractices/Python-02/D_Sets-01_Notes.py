# SETS in Python
# A set is an unordered collection of unique elements.
# Sets are defined using curly braces {} or the set() function.

# Create a set of music genres
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1
# the output will show only unique elements, so "rock" will appear only once:
# {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}

# We can  convert list to set by using the set() function. This will remove any duplicate elements from the list.
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres

# ---- SET OPERATIONS ----
# We can add an element to a set using the add() method. If the element already exists in the set, it will not be added again.

#sample set A:
A = set(["Thriller", "Back in Black", "AC/DC"])
A   # {'AC/DC', 'Back in Black', 'Thriller'}

# Add "NSYNC" to set A
A.add("NSYNC")
A   # {'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'}

# Add "NSYNC" again to set A
A.add("NSYNC")
A   # {'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'} - "NSYNC" is not added again because it already exists in the set

# Remove the element from set using the remove() method. If the element does not exist in the set, it will raise a KeyError.
A.remove("NSYNC")
A   # {'AC/DC', 'Back in Black', 'Thriller'} - "NSYNC" has been removed from the set

# Verify if the element is in the set using the in keyword. This will return True if the element is in the set, and False otherwise.
"AC/DC" in A    # True - "AC/DC" is in the set A
"NSYNC" in A    # False - "NSYNC" is not in the set

# ---- SETS LOGIC OPERATIONS ----
# We can perform logic operations on sets such as union, intersection, difference and symmetric difference.

# Sample sets album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
album_set1, album_set2  # ({'AC/DC', 'Back in Black', 'Thriller'}, {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'})

# Find the intersections using the & operator
intersection = album_set1 & album_set2
intersection   
    # {'AC/DC', 'Back in Black'} - the intersection of the two sets is the set of elements that are common to both sets

# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)   
    # {'AC/DC', 'Back in Black'} - the intersection of the two sets is the set of elements that are common to both sets

# Find the difference in set1 but not set2
album_set1.difference(album_set2)   
    # {'Thriller'} - the difference of set1 and set2 is the set of elements that are in set1 but not in set2

# Find the difference in set2 but not set1
album_set2.difference(album_set1)  
    # {'The Dark Side of the Moon'} - the difference of set2 and set1 is the set of elements that are in set2 but not in set1

# Find the union of two sets using the union method. 
# The union of two sets is the set of all elements that are in either set1 or set2 or in both sets.
album_set1.union(album_set2)
    # {'AC/DC', 'Back in Black', 'The Dark Side of the Moon', 'Thriller'} 

# Check if superset - A set A(album_set1) is a superset of set B(album_set2) if all elements of set B are also in set A.
set(album_set1).issuperset(album_set2)   
    # False - set1 is not a superset of set2 because it does not contain all elements of set2

# Check if subset - A set A(album_set2) is a subset of set B(album_set1) if all elements of set A are also in set B.
set(album_set2).issubset(album_set1)     
    # False - set2 is not a subset of set1 because it does not contain all elements of set1

# Check if subset - A set A({"Back in Black", "AC/DC"}) is a subset of set B(album_set1) if all elements of set A are also in set B.
set({"Back in Black", "AC/DC"}).issubset(album_set1) 
    # True - the set {"Back in Black", "AC/DC"} is a subset of set1 because all elements of the set are also in set1

# Check if superset - A set A(album_set1) is a superset of set B({"Back in Black", "AC/DC"}) if all elements of set B are also in set A.
album_set1.issuperset({"Back in Black", "AC/DC"})  
    # True - set1 is a superset of the set {"Back in Black", "AC/DC"} because it contains all elements of the set
    