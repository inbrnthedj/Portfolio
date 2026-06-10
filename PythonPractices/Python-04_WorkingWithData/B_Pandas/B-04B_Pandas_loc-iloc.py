'''
loc() and iloc() functions are data selecting methods in python

loc()
- used for label-based indexing

- we used the name of the row or column we want to select
    - loc[row_label, column_label]
iloc()
- used for integer-based indexing
- we use the number/index of specific row/column we want to select
    - iloc[row_index, column_index]
'''


# Import Pandas
import pandas as pd

#Define a dictionary 'x1'

x1 = {'Student': ['David','Samuel', 'Terry', 'Evan'], 
     'Age': ['27', '22', '23', '21'], 
     'Country': ['USA', 'Canada', 'UK', 'Australia'], 
     'Course': ['Computer Science', 'Software Engineering', 'Design', 'Infrastructure'], 
     'Marks':[85, 90, 78, 92]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x1)

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the column using the name
df.loc[0, 'Salary']
