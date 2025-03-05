#!/usr/bin/env python3

"""
Title: Call My Module in Python3
Author: Alan MacDonald
Date: 04/03/2025

This program demonstrates the use of calling own
modules in Python3.

Observations:
- I had to remove the main function in my_module2.py,
as it was causing a conflict with the main function in
this program.
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

from my_module2 import range_prod
import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #


# List of 5 tuples
list_ = ((5,), (2, 5), (3, 5), (4, 5), (5, 5))

# -------------------------------------------- #
# //               Main function            // #
# -------------------------------------------- #


def main():
    """This is the main() function"""
    # loop through the tuples in list_
    for tuple_ in list_:
        x, y, z = range_prod(*tuple_)
        print(f"CALL: The product of the range from {x} .. {y} = {z}")
# END function main()

# ========================================== #
# //          Global environment          // #
# ========================================== #


# # Call main function
if __name__ == "__main__":
    main()
else:
    sys.exit(1)

# Exit program
sys.exit(0)
# END
