# While Loop Example: printing through a list using an index i
# until a certain condition is met (in this case, until we get the year 1973)

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0] # returns 1982

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]

print("It took ", i ,"repetitions to get out of loop.")

''' PROCESS:
i = 0, year = 1982, condition is true, print 1982
while(year != 1973):    |   year is 1982 != 1973, condition is true
    print(year)         |   prints 1982
    i = i + 1           |   i=0+1
    year = dates[i]     |   year = dates[1] = 1980

i = 1, year = 1980, condition is true, print 1980
while(year != 1973):    |   year is 1980 != 1973, condition is true
    print(year)         |   prints 1980  
    i = i + 1           |   i=1+1
    year = dates[i]     |   year = dates[2] = 1973

i = 2, year = 1973, condition is false, exit loop

print("It took ", i ,"repetitions to get out of loop.") 

prints "It took 2 repetitions to get out of loop."
'''