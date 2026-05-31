''' PANDAS LIBRARY

Pandas is a popular open-source data manipulation and analysis for Python
    - structured data
    - handle data in various formats

KEY FEATURES
> DATA STRUCTURES - 2 primary data structures: DataFrame and Series:
    1) DataFrame:   two-dimensional, size-mutable and tabular data structure with labeled axes (rows and columns)
    2) Series:      one-dimensional labeled array - a single column or a row of data

> DATA IMPORT AND EXPORT: can read and export data of various sources/format

> DATA MERGING AND JOINING: can combine multiple DataFrames using merge and join, similar to SQL

> EFFICIENT INDEXING: provides efficient indexing and selection methods to access specific rows and columns of data quickly

> CUSTOM DATA STRUCTURES:  can create custom data structures and manipulate data in ways that suits specific needs


'''

# FOR RELATIVE PATH

from pathlib import Path

script_dir = Path(__file__).parent

# Import panda
import pandas as pd

# Read the CSV file into a DataFrame

file_path = script_dir / "file.csv"
df = pd.read_csv(file_path)
print(df)


