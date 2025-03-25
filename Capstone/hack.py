#!/usr/bin/env python3

"""
Title: analyseCSO.py - analyse CSO data
Author: Alan MacDonald
Date: 04/03/2025

This program demonstrates multiple aspets of the
course material

Observations:
- I got the information on downloading the json file
from the following website:
https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script

"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

import csv
import urllib.request
import json
import sys
import logging
from tabulate import tabulate

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #


LETTERG_CSV = "letterG.csv"
LETTERK_CSV = "letterK.csv"
CSV_HEADER = [
    "town_code",
    "town_name",
    "pop_value",
    "males_value",
    "females_value",
    "ph_occ_value",
    "ph_unocc_value",
    "vac_dwell_value",
    "h_stock_value",
    "vac_rate_value",
]

# ============================================ #
# //           getCounty Function           // #
# ============================================ #


def getCounty(town: str):
    """
    Given a string of Town data, return the county name
    Also check to see if there is a comma in the county name,
    and discard from there to the end of the string
    """
    posCounty: int = town.find("Co.")
    county = town[posCounty + 4:]
    logging.info(f"Position of Co. in {town} is {posCounty},"
                 f" county is {county}")
    if county.find(",") != -1:
        logging.info("There is a comma in the county name")
        posComma = county.find(",")
        logging.info(f"The comma position is {posComma}")
        logging.info(f"The corrected county name is " f"{county[:posComma]}")
        county = county[:posComma]

    return county


# ============================================ #
# //            getTown Function            // #
# ============================================ #


def getTown(town: str):
    """
    Given a string of Town data, return the town name
    """
    posCounty: int = town.find("Co.")
    town = town[3:posCounty - 1]
    return town

def townLetter(theTowns, letter):

    townList = {}

    for key, town in theTowns.items():
        if town[4] == letter:
            townList[key] = town
    return townList

def buildData(smallTownList, valuesList):
    townData = []

    print(f"The smallTownList is {smallTownList}")
    for key, town in smallTownList.items():

        print("should see several of me")

    return townData

# -------------------------------------------- #
# //               Main function            // #
# -------------------------------------------- #


def main():
    """This is the main() function"""
    # Set the logging level to info
    logging.basicConfig(level=logging.WARNING)

    # Pull the JSON data from the supplied URL
    with urllib.request.urlopen(
        "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CD176/JSON-stat/1.0/en"
    ) as url:
        data = json.load(url)
        logging.info(data)

    # Save the data to a json file in the current working directory
    # called CSO.json
    try:
        outfile = open("CSO.json", "w")
        json.dump(data, outfile)
        outfile.close()
    except IOError as e:
        logging.error(f"Failed to write to 'CSO.json': {e}")
        sys.exit(1)

    # Import CSO.json to a dictionary
    try:
        infile = open("CSO.json", "r")
        data = json.load(infile)
        infile.close()
    except IOError as e:
        logging.error(f"Failed to open 'CSO.json': {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error while opening 'CSO.json': {e}")
        sys.exit(1)

    # Build a lookup list from $.dataset.dimension.C03198V03862.category.label
    # This will allow us to look up the population data later
    lookup = {}
    for key, value in data["dataset"]["dimension"]["C03198V03862"]["category"][
        "label"
    ].items():
        # Set the value to be the first 3 characters of the value item
        value = value[0:3]
        lookup[value] = key

    logging.info("Lookup List")
    logging.info(lookup)

    # Extract a list of all values from $.dataset.value
    values = data["dataset"]["value"]
    logging.info("List of all values")
    logging.info(values)
    logging.info(type(values))

    # make a list of all the towns
    allTowns = {}

    logging.info("Building list of all towns")

    allTowns = data["dataset"]["dimension"]["C03198V03862"]["category"]["label"]
    logging.info("***List of all towns")
    logging.info(type(allTowns))
    logging.info(allTowns)

    # EXTRACT THE DATA FOR TOWNS STARTING WITH G
    # Declare a dictionary called gTowns
    gTowns = {}
    logging.info("Building dictionary of G towns")

    gTowns = townLetter(allTowns, "G")
    print(f"The gTowns is {gTowns}")
    # # step through the list of towns in allTowns
    # for key, town in allTowns.items():
    #     # print(f"Town: {town}")
    #     if town[4] == "G":
    #         # add town to dictionary gTowns with key index
    #         gTowns[key] = town

    logging.info("***Dictionary of G towns")
    logging.info(gTowns)

    # So we have our list of G towns in a dictionary.
    # We now need to step through the items in the dictionary,
    # extract the index, use that index to lookup the data in
    # the values list, and append it to CSV_Data

    CSV_Data = []

    logging.info(CSV_HEADER)

    CSV_Data.append(CSV_HEADER)

    print(f"The CSV_Data is {CSV_Data}")
    print(f"gTowns is {gTowns}")
    CSV_Data = buildData(gTowns, values)

    print(f"The CSV_Data is {CSV_Data}")


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
