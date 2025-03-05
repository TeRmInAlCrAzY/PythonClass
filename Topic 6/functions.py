#!/usr/bin/env python3

"""
Title: Functions in Python3
Author: Alan MacDonald
Date: 04/03/2025

This program demonstrates the use of functions in Python3.

Observations:
- There is a requirement to use a help function - I found
the built in help() function and used that, but I am not sure
if this is the best way to do it. The help function we
discussed in class seemed to be for programs that accepted
and documented command line arguments, which this program does not.
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

from tools import *
import sys

# ============================================ #
# //                Functions               // #
# ============================================ #

# -------------------------------------------- #
# //          my_function function          // #
# -------------------------------------------- #


# START function my_function
def my_function(required, *args, **kwargs):
    """
    This is a function that accepts 3 types of arguments.
    1. A required variable
    2. Any number of additional variables
    3. Any number of key/value sets
    """

    # Use a function help statement to print information about the function.
    help(my_function)

    # Print out the various arguments
    printHeader("Required Variable")
    print(f"Required: {required}")

    printHeader("Additional Variables")
    for arg in args:
        print(f"Additional: {arg}")

    printHeader("Key/Value Sets")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    # Return a list including all the data received
    return [required, args, kwargs]
# END function my_function

# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #


# START function main()
def main():
    # Create a variable, list_ and load it from the function my_function
    list_ = my_function("This is a required variable",
                        "This is an additional variable",
                        6,
                        "Favourite fruit is Peach",
                        "Next we will have key/value variables",
                        first_name="Alan",
                        surname="MacDonald",
                        age=55,
                        status="Student")

    # Loop through the list and print out each element
    printHeader("List")
    for item in list_:
        print(item)
# END function main()

# ========================================== #
# //          Global environment          // #
# ========================================== #


# Call main function
if __name__ == "__main__":
    main()
else:
    sys.exit(1)

# Exit program
sys.exit(0)

# END
