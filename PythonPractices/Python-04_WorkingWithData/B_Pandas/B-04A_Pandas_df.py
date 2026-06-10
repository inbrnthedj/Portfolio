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

# Retrieve Marks column to variable a1
a1 = df[['Marks']]
print(a1)

# Retrieve Country and course columns to variable b1
b1 = df[['Country', 'Course']]
print(b1)

# retrieve column as Series
c1 = df['Student']
print(c1)
print(type(c1))
