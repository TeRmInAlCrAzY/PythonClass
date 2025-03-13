#! /usr/bin/env python3

"""
Title: .csv File Handling in Python3
Author: Alan MacDonald
Date: 13/03/2025

This program demonstrates the use of .csv
file handling in Python3.
"""
# ============================================ #
# //             Module imports             // #
# ============================================ #

import csv
import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #


ORDERS_CSV = "orders.csv"
ORDERS2_CSV = "orders2.csv"
NEW_DATA = ["14/5/2021", "West", "Duggan", "Stapler", "5", "15", "75"]

# -------------------------------------------- #
# //               Main function            // #
# -------------------------------------------- #


def main():
    """This is the main() function"""

    header = list()
    data = list()

    # Read in the source .csv file
    try:
        fh = open(ORDERS_CSV, mode="r", encoding="utf8")
    except FileNotFoundError as e:
        print(f"ERROR: File '{ORDERS_CSV}' not found.")
        print(f"Logging: {e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"ERROR: Permission denied for file '{ORDERS_CSV}'.")
        print(f"Logging: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: New un-excepted error.h")
        raise OSError(e)

    csv_read = list(csv.reader(fh))
    header = csv_read[0]
    data = csv_read[1:]

    # Add on the extra data
    data.extend([NEW_DATA])

    # Write out the updated data file
    try:
        fh = open(ORDERS2_CSV, mode="w", encoding="utf8")
    except PermissionError as e:
        print(f"ERROR: Permission denied for file '{ORDERS_CSV}'.")
        print(f"Logging: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: New un-excepted error.h")
        raise OSError(e)

    csv_write = csv.writer(fh)
    csv_write.writerow(header)
    csv_write.writerows(data)


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
