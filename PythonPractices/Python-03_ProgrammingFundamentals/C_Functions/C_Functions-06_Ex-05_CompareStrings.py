'''Compare strings using == operator and IF-ELSE in a function'''

# 1 - User-Defined function to compare two strings
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# 2 - Declare two different variables as string1 and string2 and pass string in it
string1 = "The BodyGuard is the best album"
string2 = "The BodyGuard is the best album"

# 3 - Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

# 4 - Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")