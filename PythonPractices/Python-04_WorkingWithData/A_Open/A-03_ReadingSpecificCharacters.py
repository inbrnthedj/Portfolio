'''
This python file aims to access specific characters from a file
We are goint to use the seek() method. It moves the file pointer like a cursor to a particular position
file.seek(position)

position is a number refered to the nth position in bytes
after the seek() method, if we use the read() method, it will start on that position.
'''

from pathlib import Path

script_dir = Path(__file__).parent

file_path = script_dir / "file.txt"

with open(file_path, "r") as file:
    while True:
        line = file.readline()
        if not line:
            print("-----END----")
            break       #stops loop
        print(line.strip())
    content=file.seek(10)
    print(content)
    characters = file.read(5)
    print(characters)