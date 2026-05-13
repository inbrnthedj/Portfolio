

# 1 - Convert the list ['rap','house','electronic music', 'rap'] to a set:
music_genres = set(['rap', 'house', 'electronic music', 'rap'])

# 2 - Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
sum_A = sum(A)  # sum(A) is: 6
sum_B = sum(B)  # sum(B) is: 3
print("Does sum(A) == sum(B)?")
print(sum_A == sum_B)  # This will print: False, because 6 is not equal to 3

# 3 - Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print("The union of album_set1 and album_set2 is:")
print(album_set3)  # This will print: {'AC/DC', 'Back in Black', 'Thriller', 'The Dark Side of the Moon'}

# 4 - Find out if album_set1 is a subset of album_set3:
album_set1.issubset(album_set3) # This will return True, because all elements of album_set1 are also in album_set3
# For a better understanding, we can also print the result:
is_subset = album_set1.issubset(album_set3)
print("Is album_set1 a subset of album_set3?")
print(is_subset)  # This will print: True, because all elements of album_set1 are also in album_set3