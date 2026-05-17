'''
 While loop is used to exeute a block of code when we don't
know how many times we want to execute the block of code.
That is, if we want to execute a block of code until a certain condition is met, 
we can use a while loop.

 Syntax of while loop:
 while condition:
        # block of code to be executed
    The condition is evaluated before the execution of the block of code.
    The block of code will be executed as long as the condition is true.

'''

# Example:
i = 1
while i <= 5:
    print(i)
    i += 1

# This will print the numbers from 1 to 5. 
# The loop will continue to execute as long as the condition i <= 5 is true. 
# Once i becomes 6, the condition will be false and the loop will stop executing.