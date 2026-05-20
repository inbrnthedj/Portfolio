'''FileNotFound Error'''
# accessing a non-existent file
with open("nonexistent_file.txt", "r") as file:
        content = file.read()   # Raises FileNotFoundError