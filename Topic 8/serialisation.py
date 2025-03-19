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

YAML_FILE = "network.yaml"
JSON_FILE = "network.json"


def main():
    """This is the main() function"""
    # Set the logging level to info
    logging.basicConfig(level=logging.WARNING)


    print(f"Reading the '{YAML_FILE}' YAML file")
    fh = open(YAML_FILE, mode="r", encoding="utf8")
    head_ = fh.readline()
    net_list = yaml.safe_load(fh)
    fh.close()

    print(f"ens192: {str(net_list['network']['ethernets']['ens192']['addresses'])[2:-2]}")
    print(f"ens224: {str(net_list['network']['ethernets']['ens224']['addresses'])[2:-2]}")

    print(f"Serialising data to'{JSON_FILE}'")
    fh = open(JSON_FILE, mode="w", encoding="utf8")
    json.dump(net_list, fh, indent=4)

    fh = open(YAML_FILE, mode="r", encoding="utf8")
    data = yaml.full_load(fh)
    logging.info(f"The type of the data is {type(data)}")
    logging.info("The contents of the data")
    logging.info(data)
    logging.info(f"{data.get('network').get('ethernets').get('ens192').get('addresses')}")
    mystring=str(data.get('network').get('ethernets').get('ens192').get('addresses'))


    logging.info(f"The type of the string is {type(mystring)}")
    logging.info(f"The string is {mystring}")
    logging.info(f"The string is {mystring[2:-2]}")

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
