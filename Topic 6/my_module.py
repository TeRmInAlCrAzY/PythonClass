#!/usr/bin/env python3

"""
Title: Modules in Python3
Author: Alan MacDonald
Date: 04/03/2025

This program demonstrates the use of modules in Python3.
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

# from tools import *
import math
import sys

# ============================================ #
# //                Functions               // #
# ============================================ #

# -------------------------------------------- #
# //          range_prod function           // #
# -------------------------------------------- #


# START function range_prod()
def range_prod(*args):
    """
    Name : Product of Range between two numbers
    """
    arguments = tuple(args)

    if len(arguments) == 1:
        r1 = 1
        r2 = arguments[0]
    else:
        r1 = arguments[0]
        r2 = arguments[1]

    list_ = list(range(r1, r2+1))
    # printHeader("The contents of the list")
    # print(list_)

    # printHeader("The product of the range")
    ans = math.prod(list_)
    # print(f"The product of the range is {ans}")

    return r1, r2, ans
# END function range_prod()

# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #


# START function main()
def main():
    """
    This is the main part of the program.
    It defines a default variable, calls the range+prod function,
    traps the return values and prints them.
    """

    default_variable = 5

    a, b, c = range_prod(default_variable)

    # printHeader("Main Output")
    print(f"MOD: The product of the range from {a} .. {b} = {c}")
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
