''' 
SERIES
> one-dimensional labeled array in pandas
> can be created from various data sources:
    - lists
    - NumPy arrays
    - dictionaries

SERIES ATTRIBUTES
> values: 
    Returns the Series data as a NumPy array.
> index: 
    Returns the index (labels) of the Series.
> shape: 
    Returns a tuple representing the dimensions of the Series.
> size: 
    Returns the number of elements in the Series.
> mean(), sum(), min(), max(): 
    Calculate summary statistics of the data.
> unique(), nunique(): 
    Get unique values or the number of unique values.
> sort_values(), sort_index(): 
    Sort the Series by values or index labels.
> isnull(), notnull(): 
    Check for missing (NaN) or non-missing values.
> apply(): 
    Apply a custom function to each element of the Series.


'''
# IMPORT PANDAS
import pandas as pd

# CREATE SERIES FROM LIST
data = [10, 20, 30, 40, 50] # NOTE: labels in lists starts with 0
s = pd.Series(data)
print(s)

# ACCESS ELEMENTS IN SERIES BY LABEL
print(s[2])     # returns the element with label 2 (value 30)

# ACCESS ELEMENTS IN SERIES BY POSITION
print(s.iloc[3]) # Access the element at position 3 (value 40)

# ACCESSING MULTIPLE ELEMENTS
print(s[1:4])   # Access elements with label from 1 to 3 (excluding label 4, therefore all except 10, 50)
