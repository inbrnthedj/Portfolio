''' READLINES

readline()
    - reads the file line by line as an element in a list
    - reads the file in order


'''

# 1 -------- use pathlib
from pathlib import Path

script_dir = Path(__file__).parent

file_path = script_dir / "file.txt"

with open(file_path, "r") as file:
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)

print(file.closed)

# We can use a loop to read until no more lines are left
with open(file_path, "r") as file:
    while True:
        line = file.readline()
        if not line:
            print("-----END----")
            break       #stops loop
        print(line.strip()) # strip() removes the newline character at the end of every line


