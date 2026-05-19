'''
Functions and loops together:
- Functions can contain code with loops
- This makes complex tasks more organized
- The loop code becomes a repeatable function

Enhancing code organization and reusability
- Functions group similar actions for easy understanding
- Looping within functions keeps code clean
- You can reuse a function to repeat actions
'''

# Example: A function that greets name input
def greet(name):
    '''This function prints a greeting for a given name.'''
    print(f"Hello, {name}! Welcome to Python programming.")

for i in range(3): # Loop to greet three different names
    name = input("Enter a name to greet: ")
    greet(name) # Call the greet function with the input name

