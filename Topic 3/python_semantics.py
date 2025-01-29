#!/usr/bin/env python3

""" Python3 Semantics Exercise"""

import os

#Assign integer variables
int1=int2=int3=2

# Add 1 to int3
int3+=1

# Perform calculation and assign to a variable with number and underscore
result_1=(int1*int3)*int2

# Get user input
in_=input("Please enter a number between 1 and 99: ")

# Print received number
print(f"I have received the number {in_}")

# Convert input to integer
in_=int(in_)

# Perform division and assign to underscore variable
_=in_/result_1

# Print underscore variable contents
print(f"The result of the division is {_}")

# Print files an directories in the current directory
print(f"Files and directories in current directory: {os.listdir()}")

# Print files and directories in the current directory, but prettier
print(f"Files and directories in current directory:\n")
for item in os.listdir():
    print(item)
