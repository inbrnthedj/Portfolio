'''
SCOPE is where a variable can be seen and used:
- Local Scope: 
    Variables defined within a function are only accessible within that function.
- Global Scope: 
    Variables defined outside of any function are accessible throughout the entire program,
    , including inside functions.
'''

# Example of local scope
def local_scope_example():
    local_variable = "I am a local variable."
    print(local_variable)
local_scope_example()

# This will raise an error because local_variable is not defined outside the function:
# print(local_variable) 

# Example of global scope
global_variable = "I am a global variable."
def global_scope_example():
    print(global_variable)
global_scope_example()

# This will work because global_variable is defined in the global scope:
print(global_variable)