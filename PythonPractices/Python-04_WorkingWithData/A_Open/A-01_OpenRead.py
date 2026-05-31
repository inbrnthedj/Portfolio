'''FILE HANDLING WITH read() AND open()

We can open a file in python by using open():
file=open("filedirectory/filename",mode)     
values for mode:
    - "r" for read only
    - "w" for writing
    - "a" for appending

ATTRIBUTES AND METHODS FOR FILES:
file.name:      a string that contains name of file
file.mode:      returns 'r', 'w' or 'a'
file.close():   closes the file

we can also use a with statement because it automatically closes the file
whith open("file.txt","r") as file1:
    file_stuff = file1.read()
    print(file_stuff)

print(file1.closed)
print(file_stuff)

FOR RELATIVE SOURCE PATH:
We may use two different methods:
1) pathlib
2) os module

'''

# 1 -------- use pathlib
from pathlib import Path

script_dir = Path(__file__).parent

file_path = script_dir / "file.txt"

with open(file_path, "r") as file:
    content = file.read()

print(file.closed)  # This will return true if the file is closed (thanks to with statement)
print(content)      # this will print the text because the variable "content" read the document


# 2 -------- use os module
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


file_path = os.path.join(script_dir, "file.txt")

# Open the file in read ('r') mode
with open(file_path, "r") as file:
    content = file.read()

print(file.closed)  # This will return true if the file is closed (thanks to with statement)
print(content)      # this will print the text because the variable "content" read the document

