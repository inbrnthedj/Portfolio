# For loop example: printing through a list using index

# my list
dates = [1982,1980,1973]
# getting total numbers of items in the list
N = len(dates) # N is 3 in this case, as there are 3 items in the list
# NOTE that in lists, index starts with 0

# basic for loop to print each item in the list
for i in range(N): # i starts with 0 and goes up to N-1, that is 2 in this case
    print(dates[i])   

# We can also write:
for year in dates: # for each iteration, the value of the variable year behaves like the value of dates[i]
    print(year) 