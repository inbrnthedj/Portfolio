'''
BREAK and CONTINUE statements are used to control the flow of loops in Python.
    - BREAK : used to exit a loop prematurely when a certain condition is met.
    - CONTINUE : used to skip the current iteration of a loop and move on to the next iteration.

'''
# Example of BREAK statement in a for loop
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)

# Example of CONTINUE statement in a for loop
for num in range(1, 10):
    if num == 5:
        print("Skipping the number:", num)
        continue
    print(num)

# Example of BREAK statement in a while loop
i = 1
while i <= 10:
    if i == 5:
        print("Breaking the loop at:", i)
        break
    print(i)
    i += 1

# Example of CONTINUE statement in a while loop
i = 1
while i <= 10:
    if i == 5:
        print("Skipping the number:", i)
        i += 1
        continue
    print(i)
    i += 1
