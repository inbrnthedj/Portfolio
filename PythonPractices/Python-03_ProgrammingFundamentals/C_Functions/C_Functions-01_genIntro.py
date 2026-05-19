''' FUNCTIONS IN PYTHON
The function is a block of code which only runs when it is called. 
You can pass data, known as parameters, into a function. A function 
can return data as a result.

In python, there are in-built functions and user-defined functions. 
Some built-in functions are:
- print(): prints the specified message to the screen, or other standard output device.
- len(): returns the number of items in an object.
- type(): returns the type of the specified object.
- int(): converts a specified value into an integer number.
- str(): converts a specified value into a string.
- float(): converts a specified value into a floating-point number.


USER-DEFINED FUNCTIONS
A user-defined function is a function that you create to perform a specific task.
To create a function, you use the def keyword, followed by the function name and parentheses.
The syntax for defining a function is as follows:
def function_name(parameters):
    docstring
    function body
    return value
'''

# Example of a user-defined function
def area_of_rectangle(length, width):
    '''This function calculates the area of a rectangle.'''
    area = length * width
    return area

# Let's call the function and print the result
length = 5
width = 3
result = area_of_rectangle(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {result}.")

# Functions don't even have to return anything. They can just perform an action.
def print_greeting(name):
    '''This function prints a greeting message.'''
    print(f"Hello, {name}! Welcome to Python programming.")

# Let's call the function to see the greeting message
print_greeting("World")
