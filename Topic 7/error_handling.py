#! /usr/bin/env python3

"""
Title: Error Handling in Python3
Author: Alan MacDonald
Date: 05/03/2025

This program demonstrates the use of error handling in Python3.
"""

my_List = ('1', 2, 3, '4', 'A', 5, 6, '7')

# create a loop that prints the type and value of each element in my_list
# the print() statement should use end = to prevent carriage return
for element in my_List:
    print(f"{type(element)} {element}", end=" ")

    try:
        attempt_int = int(element)
        print(f" now {type(attempt_int)} {attempt_int}")
    except ValueError:
        print(f" now ")