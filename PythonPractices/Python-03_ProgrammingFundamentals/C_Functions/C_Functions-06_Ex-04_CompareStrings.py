''' Using If-Else in a function to compare strings'''

#Compare Two Strings Directly using in operator
# declare string
string= "The BodyGuard is the best album"

# Define a funtion
def check_string(text1):
    # Use if else statement and 'in' operatore to compare the string
    if text1 in string:
        return 'String matched'
    else:
        return 'String not matched'

result_check=check_string("The BodyGuard is the best")
print(result_check)
