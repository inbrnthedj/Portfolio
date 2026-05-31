''' PYTHON'S open() FUNCTION

open() function can create a new text file and write data in Python
arguments:
    - file path, including file name and extension
    - mode paramenter:
        - 'r'   :   read-only
        - 'a'   :   append
    >   - 'w'   :   write
    >   - 'x'   :   exclusive creation mode - creats new file for writing (might raise error if file already exists)
        - 'rb'  :   read binary mode - opens an existing binary file for reading
    >   - 'wb'  :   write binary mode - creates new binary file
        - 'ab'  :   append binary mode. open and appends data of binary file
    >   - 'xb'  :   exclusive binary creation mode
        - 'rt'  :   read text mode - opens an existing file for reading
    >   - 'wt'  :   write text mode - creates new text file for writing
        - 'at'  :   append text mode - opens and appends data of text file
        - 'xt'  :   exclusive text creation mode - creates new text file for writing (might raise error if file exists)
    >   - 'r+'  :   read and write mode. Opens an existing file for both reading and writing
    >   - 'w+'  :   write and read mode. creates new file for reading and writing. overwrites file if existing
        - 'a+'  :   append and read mode. opens a file for appending and reading. creates file if non-existent
    >   - 'x+'  :   exclusive creation and read/write mode - creates new file for reading and writing but raises an error if file exists

To write a file, we need to use the mode 'w'   

'''
# ------------ USE PATHLIB FOR RELATIVE SOURCE PATH
from pathlib import Path

script_dir = Path(__file__).parent

file_path = script_dir / "Example.txt"

# ------------- FILE CREATION/WRITING
# List of lines to write to the file
Lines = ["This is line 1.", "This is line 2.", "This is line 3."]

# Create a new file Example.txt for writing 
# 'w' creates the file if non-existing and overwrites it if it exists
with open(file_path, 'w') as file0:
    for line in Lines:
        file0.write(line + "\n")
    # file0 is automatically closed when the 'with' block exits

# ------------- APPENDING DATA TO AN EXISTING FILE
# to append data, we use 'a' mode

new_data = "This is line D."

file_path1 = script_dir / "Example1.txt"

# Open an existing file Example1.txt for appending
with open(file_path1, 'a') as file1:
    file1.write(new_data + "\n")
    # file1 is automatically closed when the 'with' block exits

# ------------- COPYING CONTENTS FROM ONE FILE TO ANOTHER

fileSource_path = script_dir / "Example.txt"
fileDest_path = script_dir / "Example2.txt"

with open(fileSource_path, 'r') as source_file:
    # Open the destination file for writing
    with open(fileDest_path, 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits
