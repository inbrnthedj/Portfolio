# Branching allows us to execute different code based on conditions. 
# In Python, we use if, elif, and else statements for branching.

# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Spongebob" )
    
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")