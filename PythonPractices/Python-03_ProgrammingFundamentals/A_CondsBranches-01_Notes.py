# Start of Programming Fundamentals - Conditions and Branches Notes
'''
1. Conditional Statements

Equality and Comparison Operators:
- == : Equal to
- != : Not equal to
- >  : Greater than
- <  : Less than
- >= : Greater than or equal to
- <= : Less than or equal to

Logical Operators:
- and : Returns True if both statements are true
- or  : Returns True if one of the statements is true
- not : Reverses the result, returns False if the result is true

'''
3==5 # False
3!=5 # True
i=5
i>3 # True
i<3 # False
i>=3 # True
i<=3 # False

1==1 and 2==2 # True - BOTH True
1==1 and 2==3 # False - ONE False
1==1 or 2==3 # True - ONE True
1==2 or 2==3 # False - BOTH False
not 1==1 # False - 1==1 is True, so not True is False
not 1==2 # True - 1==2 is False, so not False is True

'''
2. If Statements
Syntax:
if condition:
    # code to execute if condition is true
Example: '''

age = 18
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are eligible to drive.")
else:
    print("You are not eligible for any privileges.")


