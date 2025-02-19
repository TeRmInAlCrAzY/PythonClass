#!/usr/bin/env python3

"""
Title: Iteration in Python3
Author: Alan MacDonald
Date: 19/02/2025

This program demonstrates the use of iteration in Python3.

Observations:
-
"""

# Create a range from 1- 100 and with a for loop print the square of the current number
for x in range(1, 100):
    print(f'{x * x}')
    # Add logic to break if square of x >= 6400
    if x * x >= 6400:
        # Message explaining why we are breaking out of the loop
        print("Broke out of loop as x^2 > 6400")
        break

