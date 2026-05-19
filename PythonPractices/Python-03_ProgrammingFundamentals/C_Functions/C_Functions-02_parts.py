'''
Benefits of using functions
- Modularity: Functions break down complex tasks into manageable components
- Reusability: Functions can be used multiple times without rewriting code
- Readability: Functions with meaningful names enhance code understanding
- Debugging: Isolating functions eases troubleshooting and issue fixing
- Abstraction: Functions simplify complex processes behind a user-friendly interface
- Collaboration: Team members can work on different functions concurrently
- Maintenance: Changes made in a function automatically apply wherever it's used

INPUT (PARAMETERS)
Functions operate on data and can receive data as input, or "parameteres"/"arguments".
They provide functions with the necessary information to perform their tasks.

PERFORMING TASKS
Once function receives parameters, it executes predefined operations that can
include calculations, data manipulation or eveno more complex tasks.

OUTPUT (RETURN VALUES)
Functions produce an output, which is the result of the operations carried out within
the function and is called the "return value". 


'''


# EXAMPLE: SUM OF TWO NUMBERS
def SUM2(a, b):
    total2 = a + b
    return total2

result = SUM2(5,7)
print(f"The sum of 5 and 7 is: {result}.")