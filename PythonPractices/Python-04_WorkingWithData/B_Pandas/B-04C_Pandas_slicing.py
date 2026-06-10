'''
Slicing uses the [] operator to select a set of rows and/or columns
    - df[first_row:last_row_excluded, first_column:last_column_excluded]

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

# print first two rows and first three columns
print(df.iloc[0:2, 0:3])

# slicing using loc() function
print(df.loc[0:2,'Student':'Course'])