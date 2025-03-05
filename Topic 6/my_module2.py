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
