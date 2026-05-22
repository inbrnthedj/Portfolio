'''
Exercise 2: Handling ValueError
Create a Python function that generates the square root value if a positive integer 
or float value provided as input. The function should be detect the mistake if a 
negative value is entered. It should kindly inform you with a message saying, 
'Invalid input! Please enter a positive integer or a float value.
'''

# Import math library
from math import sqrt

def rootval(number1):
    try:
        result=sqrt(number1) # will not work if math library not imported
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter a positive integer or a float value.")


#Test Case
number1 = float(input("Enter a number to perform square root: "))
rootval(number1)