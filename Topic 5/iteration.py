#!/usr/bin/env python3

from tools import *

"""
Title: Iteration in Python3
Author: Alan MacDonald
Date: 19/02/2025

This program demonstrates the use of iteration in Python3.

Observations:
- I found instruction 6 to be ambiguous, so I have given 2 interpretations
"""

# Create a range from 1- 100 and with a for loop print the square of the current number
printHeader("Squares")
for x in range(1, 100):
    print(f'{x * x}')
    # Add logic to break if square of x >= 6400
    if x * x >= 6400:
        # Message explaining why we are breaking out of the loop
        print("Broke out of loop as x^2 > 6400")
        break

# Create a range from 10 to 100 in steps of 5 and assign it to a variable
printHeader("Range")
numbers = []
for x in range(10, 100, 5):
    numbers.append(x)

# Print the type and content of the numbers variable
print(f"The type of numbers is {type(numbers)}")
print(f"The contents of numbers is\n{numbers}")

# The requirement for the next part is very ambiguous, sorry, so I have given 2
# of the many, many interpretations

# Print the numbers of the list with '--' between each number, using enumerate
# This prints a vertical list with -- between each element of the enumeration
printHeader("Enumerate 1")

for count, number in enumerate(numbers):
    print(f"{count + 1}--{number}")

# Print the numbers of the list with '--' between each number, using enumerate
# This prints a horizontal list with -- between each element of the enumeration
# It does have a single - on the start and end, but I am not going to remove it
printHeader("Enumerate 2")
for count, number in enumerate(numbers):
    print(f"-{number}-", end="")
print() # clear the line

# Convert the numbers variable to a list
# I am confused here, as it started as a list anyway :)
numbers = list(numbers)

# Use w while loop to print out the first 6 values of the list
printHeader("While")
stopcount = 6
count = 1

while count <= stopcount:
    print(f"{numbers[count-1]}")
    count += 1
