#! /usr/bin/env python3

"""
Title: yaml File Handling in Python3
Author: Alan MacDonald
Date: 13/03/2025

This program demonstrates the use of yaml
file handling in Python3.
"""
# ============================================ #
# //             Module imports             // #
# ============================================ #

import yaml
import json
import logging
import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

YAML_FILE = "network.yaml"
JSON_FILE = "network.json"

# -------------------------------------------- #
# //               Main function            // #
# -------------------------------------------- #


def main():
    """This is the main() function"""
    # Set the logging level to info
    logging.basicConfig(level=logging.WARNING)

    # Read in the YAML file with some basic error catching
    print(f"Reading the '{YAML_FILE}' YAML file")
    try:
        fh = open(YAML_FILE, mode="r", encoding="utf8")
    except FileNotFoundError:
        logging.ERROR(f"File '{YAML_FILE}' not found.")
        sys.exit(1)
    except Exception as e:
        logging.ERROR(f"An error occurred while opening '{YAML_FILE}': {e}")
        sys.exit(1)

    # Read in the YAML file data to variables
    head_ = fh.readline()
    net_list = yaml.safe_load(fh)
    fh.close()

    # Print required output
    print(
        f"ens192: "
        f"{str(net_list['network']['ethernets']['ens192']['addresses'])[2:-2]}"
    )
    print(
        f"ens224: "
        f"{str(net_list['network']['ethernets']['ens224']['addresses'])[2:-2]}"
    )

    # Write out the YAML data to a JSON file
    # Uses some basic error catching
    print(f"Serialising data to '{JSON_FILE}'")
    try:
        fh = open(JSON_FILE, mode="w", encoding="utf8")
    except PermissionError:
        logging.warning(
            f"Permission denied, unable to write to '{JSON_FILE}'.")
        sys.exit(1)
    except Exception as e:
        logging.warning(
            f"An error occurred while opening '{JSON_FILE}': {e}")
        sys.exit(1)

    # Write out the JSON file
    json.dump(net_list, fh, indent=4)
    fh.close()


# END function main()

# ========================================== #
# //          Global environment          // #
# ========================================== #


# Call main function
if __name__ == "__main__":
    main()
else:
    sys.exit(0)

# Exit program
sys.exit(0)

# END
