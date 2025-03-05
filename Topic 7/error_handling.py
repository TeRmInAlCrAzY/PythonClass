#! /usr/bin/env python3

"""
Title: Error Handling in Python3
Author: Alan MacDonald
Date: 05/03/2025

This program demonstrates the use of error handling in Python3.
"""
# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #


# List of ints and strings
my_List = ('1', 2, 3, '4', 'A', 5, 6, '7')

# -------------------------------------------- #
# //               Main function            // #
# -------------------------------------------- #


def main():
    # Loop with error checking for faults converting to int
    for element in my_List:
        print(f"{type(element)} {element} now ", end=" ")

        try:
            attempt_int = int(element)
            print(f"{type(attempt_int)} {attempt_int}")
        except ValueError:
            print(f"{element} cannot be converted to an integer")

    # Loop with no error checking for faults converting to int
    for element in my_List:
        print(f"{type(element)} {element} now ", end=" ")

        attempt_int = int(element)
        print(f"{type(attempt_int)} {attempt_int}")
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
