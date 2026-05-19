'''
Using If-Else statements and loops in a function
- usually uses return() if you have any IF statements
'''

# Identify type of album

def type_of_album(album, year_released):
    
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("The BodyGuard", 1980)
print(x)