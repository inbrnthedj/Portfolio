'''Write a Python program using a for loop that prints numbers from 1 to 15 but:

Skips multiples of 3
Stops the loop if the number is greater than 12
'''

for i in range(1, 16):
    if i % 3 == 0:
        continue  # skip multiples of 3
    if i > 12:
        break     # stop if number > 12
    print(i)