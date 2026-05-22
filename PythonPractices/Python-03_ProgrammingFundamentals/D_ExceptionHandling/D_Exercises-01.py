''' 
Exercise 1: Handling ZeroDivisionError
Create a Python function called safe_divide to determine what happens when 
you divide one number, 'numerator' by the other 'denominator'. 
Using the user input method of Python to take the values of the parameters

The function should be able to do the division and give the result. 
If the denominator is equal to zero (which is not allowed in math), the function 
should catch that and tell that it's not possible to divide by zero. 
Instead of showing an error, it should return None, which means 'nothing' or 
'no value', and print "Error: Cannot divide by Zero."
'''


def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
# Test case
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator))