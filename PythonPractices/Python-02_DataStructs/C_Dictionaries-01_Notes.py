''' DICTIONARIES IN PYTHON
Dictionaries consists of keys and values. They are unordered, mutable, and indexed by keys.
Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. 
Each key is separated from its value by a colon.

-----------------------------------------
|        LIST         |   DICTIONARY    |
|---------------------|-----------------|
|       Ordered       |    Unordered    |
|       Mutable       |     Mutable     |
| Indexed by position | Indexed by keys |
-----------------------------------------

LISTS:
|INDEX   | 0 | 1 | 2 | 3 |
|ELEMENT | A | B | C | D |

DICTIONARIES:
|KEY    | ONE  | STRING 2 | THREE 3s | THREE 4s |
|VALUE  | 1    |    '2'   |  [3,3,3] | (4,4,4)  |

Keys can be of any immutable data type (like strings, numbers, tuples), and 
values can be of any data type (including lists, dictionaries, etc.).

SYNTAX:
my_dict = {
    "key1": value1,
    "key2": value2,
    "key3": value3,
    ...
}

'''

# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

# Access to the value by the key
Dict["key1"] # This will return the value associated with "key1", which is 1.


# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

'''To understand it better:
DICTIONARY: release_year_dict
|KEY                                | VALUE  |
|-----------------------------------|--------|
|Thriller                           | '1982' |
|Back in Black                      | '1980' |
|The Dark Side of the Moon          | '1973' |
|The Bodyguard                      | '1992' |
|Bat Out of Hell                    | '1977' |
|Their Greatest Hits (1971-1975)    | '1976' |
|Saturday Night Fever               | '1977' |
|Rumours                            | '1977' |

'''

# We can retrieve the value by keys
release_year_dict['Thriller']       # returns '1982'
release_year_dict['The Bodyguard']  # returns '1992'  


# We can get all the keys in the dictionary using the keys() method
release_year_dict.keys()    
# returns dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 
# 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 
# 'Saturday Night Fever', 'Rumours'])   

# We can get all the values in the dictionary using the values() method
release_year_dict.values()
# returns dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])

# Append a new key-value pair to the dictionary 
release_year_dict['Graduation'] = '2007'
release_year_dict

# Delete entries by key using the del statement
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict    # returns True
'Graduation' in release_year_dict       # returns False
