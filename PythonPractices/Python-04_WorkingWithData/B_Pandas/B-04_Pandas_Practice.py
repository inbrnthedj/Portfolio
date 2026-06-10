# Import Pandas
import pandas as pd

#Define a dictionary 'x1'

x1 = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 
     'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
     'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x1)

#display the result df
print(df)

# Retrieve ID column and assigning to a variable y1
y1 = df[['ID']]
print(y1)
print(type(y1))

# Accessing multiple columns
z1 = df[['Department', 'Salary', 'ID']]
print(z1)