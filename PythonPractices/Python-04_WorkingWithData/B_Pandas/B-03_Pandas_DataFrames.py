'''DATAFRAMES
DataFrame:
> two-dimensional labeled data structure with columns of potentially different data types
> each column represents a variable and each row represents an observation or data point
> CSV, Excel spreadsheets, SQL databases, etc.

DATAFRAME ATTRIBUTES:
> shape: 
    Returns the dimensions (number of rows and columns) of the DataFrame.
> info(): 
    Provides a summary of the DataFrame, including data types and non-null counts.
> describe(): 
    Generates summary statistics for numerical columns.
> head(), tail(): 
    Displays the first or last n rows of the DataFrame.
> mean(), sum(), min(), max(): 
    Calculate summary statistics for columns.
> sort_values(): 
    Sort the DataFrame by one or more columns.
> groupby(): 
    Group data based on specific columns for aggregation.
> fillna(), drop(), rename(): 
    Handle missing values, drop columns, or rename columns.
> apply(): 
    Apply a function to each element, row, or column of the DataFrame.

'''

# IMPORT pandas
import pandas as pd

# CREATING DataFrames FROM DICTIONARIES
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)

# COLUMN SELECTION
print(df['Name'])  # Access the 'Name' column

# ACCESS ROWS - by index with .iloc[] or label wit .loc[]
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label

# SLICING DATAFRAMES
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

# FINDING UNIQUE ELEMENTS - .unique()
unique_dates = df['Age'].unique()

# CONDITIONAL FILTERING - inequality operators
high_above_102 = df[df['Age'] > 25]

# SAVING DATAFRAMES - .to_scv
df.to_csv('trading_data.csv', index=False)