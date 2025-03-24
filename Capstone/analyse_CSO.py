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

    for key, town in smallTownList.items():
        if town.find(",") != -1:
            posComma = town.find(",")
            town = town[:posComma]

        # Get the pop_value for each town
        adjusted_key = (int(key) - 1) * 8
        pop_value = valuesList[adjusted_key]
        males_value = valuesList[adjusted_key + 1]
        females_value = valuesList[adjusted_key + 2]
        ph_occ_value = valuesList[adjusted_key + 3]
        ph_unocc_value = valuesList[adjusted_key + 4]
        vac_dwell_value = valuesList[adjusted_key + 5]
        h_stock_value = valuesList[adjusted_key + 6]
        vac_rate_value = valuesList[adjusted_key + 7]

        townData.append(
            [
                key,
                town,
                pop_value,
                males_value,
                females_value,
                ph_occ_value,
                ph_unocc_value,
                vac_dwell_value,
                h_stock_value,
                vac_rate_value,
            ]
        )

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

    # step through the list of towns in allTowns
    for key, town in allTowns.items():
        # print(f"Town: {town}")
        if town[4] == "G":
            # add town to dictionary gTowns with key index
            gTowns[key] = town

    logging.info("***Dictionary of G towns")
    logging.info(gTowns)

    # So we have our list of G towns in a dictionary.
    # We now need to step through the items in the dictionary,
    # extract the index, use that index to lookup the data in
    # the values list, and append it to CSV_Data

    CSV_Data = []

    logging.info(CSV_HEADER)

    CSV_Data.append(CSV_HEADER)

    # Step through the gtowns
    for key, town in gTowns.items():
        # Clean the data - extra , exists in Town
        if town.find(",") != -1:
            logging.info("There is a comma in the name")
            posComma = town.find(",")
            logging.info(f"The comma position is {posComma}")
            logging.info(f"The corrected county name is {town[:posComma]}")
            town = town[:posComma]

        # Get the pop_value for each town
        adjusted_key = (int(key) - 1) * 8
        pop_value = values[adjusted_key]
        males_value = values[adjusted_key + 1]
        females_value = values[adjusted_key + 2]
        ph_occ_value = values[adjusted_key + 3]
        ph_unocc_value = values[adjusted_key + 4]
        vac_dwell_value = values[adjusted_key + 5]
        h_stock_value = values[adjusted_key + 6]
        vac_rate_value = values[adjusted_key + 7]

        CSV_Data.append(
            [
                key,
                town,
                pop_value,
                males_value,
                females_value,
                ph_occ_value,
                ph_unocc_value,
                vac_dwell_value,
                h_stock_value,
                vac_rate_value,
            ]
        )

        # logging.info(f"Town: {town} -- Population: {pop_value}")
        logging.info(
            f"{key},{town},{pop_value},"
            f"{males_value},{females_value},"
            f"{ph_occ_value},{ph_unocc_value},"
            f"{vac_dwell_value},{h_stock_value},"
            f"{vac_rate_value}"
        )

    # Open the letterG.csv file
    try:
        fh = open(LETTERG_CSV, mode="w", encoding="utf8")
    except PermissionError as e:
        print(f"ERROR: Permission denied for file '{LETTERG_CSV}'.")
        print(f"Logging: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: New un-excepted error.h")
        raise OSError(e)

    csv_writer = csv.writer(fh,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(CSV_Data)

    fh.close()

    # EXTRACT THE DATA FOR TOWNS IN COUNTIES STARTING WITH K
    # Build a list of towns in counties that start with the letter K

    # Declare a dictionary called kTowns
    kTowns = {}
    logging.info("Building dictionary of K towns")

    # Step through the list of towns in allTowns
    for key, town in allTowns.items():
        county = getCounty(town)
        if county[0] == "K":
            kTowns[key] = town

    logging.info("***Dictionary of K towns")
    logging.info(kTowns)

    CSV_Data = []

    CSV_Data.append(CSV_HEADER)

    for key, town in kTowns.items():
        # Clean the data - extra , exists in Town
        if town.find(",") != -1:
            logging.info("There is a comma in the name")
            posComma = town.find(",")
            logging.info(f"The comma position is {posComma}")
            logging.info(f"The corrected county name is {town[:posComma]}")
            town = town[:posComma]

        # Get the pop_value for each town
        adjusted_key = (int(key) - 1) * 8
        pop_value = values[adjusted_key]
        males_value = values[adjusted_key + 1]
        females_value = values[adjusted_key + 2]
        ph_occ_value = values[adjusted_key + 3]
        ph_unocc_value = values[adjusted_key + 4]
        vac_dwell_value = values[adjusted_key + 5]
        h_stock_value = values[adjusted_key + 6]
        vac_rate_value = values[adjusted_key + 7]

        CSV_Data.append(
            [
                key,
                town,
                pop_value,
                males_value,
                females_value,
                ph_occ_value,
                ph_unocc_value,
                vac_dwell_value,
                h_stock_value,
                vac_rate_value,
            ]
        )

        logging.info(
            f"{key},{town},{pop_value},"
            f"{males_value},{females_value},"
            f"{ph_occ_value},{ph_unocc_value},"
            f"{vac_dwell_value},{h_stock_value},"
            f"{vac_rate_value}"
        )

    # Open the letterK.csv file
    try:
        fh = open(LETTERK_CSV, mode="w", encoding="utf8")
    except PermissionError as e:
        print(f"ERROR: Permission denied for file '{LETTERK_CSV}'.")
        print(f"Logging: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: New un-excepted error.h")
        raise OSError(e)

    csv_writer = csv.writer(fh,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(CSV_Data)

    fh.close()

    # EXTRACT THE DATA FOR TOWNS STARTING WITH N
    # Declare a dictionary called nTowns
    nTowns = {}
    logging.info("Building dictionary of N towns")

    # Step through the list of towns in allTowns
    for key, town in allTowns.items():
        if town[4] == "N":
            # add town to dictionary nTowns with key index
            nTowns[key] = town

    logging.info("***Dictionary of N towns")
    logging.info(nTowns)

    PRINT_Data = []

    # PRINT_Data.append(CSV_HEADER)

    for key, town in nTowns.items():
        # Clean the data - extra , exists in Town
        if town.find(",") != -1:
            logging.info("There is a comma in the name")
            posComma = town.find(",")
            logging.info(f"The comma position is {posComma}")
            logging.info(f"The corrected county name is {town[:posComma]}")
            town = town[:posComma]

        # Get the pop_value for each town
        adjusted_key = (int(key) - 1) * 8
        pop_value = values[adjusted_key]
        males_value = values[adjusted_key + 1]
        females_value = values[adjusted_key + 2]
        ph_occ_value = values[adjusted_key + 3]
        ph_unocc_value = values[adjusted_key + 4]
        vac_dwell_value = values[adjusted_key + 5]
        h_stock_value = values[adjusted_key + 6]
        vac_rate_value = values[adjusted_key + 7]

        PRINT_Data.append(
            [
                key,
                town,
                "{:,}".format(int(pop_value)),
                "{:,}".format(int(males_value)),
                "{:,}".format(int(females_value)),
                "{:,}".format(int(ph_occ_value)),
                "{:,}".format(int(ph_unocc_value)),
                "{:,}".format(int(vac_dwell_value)),
                "{:,}".format(int(h_stock_value)),
                vac_rate_value,
            ]
        )

    # Now we need to print it out in a pretty fashion with columns
    # for row in PRINT_Data:
    #     print("{: <10} {: <40} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*row))

    printHeader = [
    "Code",
    "Name",
    "Population",
    "Males",
    "Females",
    "Occupied",
    "Unoccupied",
    "Dwellings",
    "Stock",
    "Vacancy %",
]
    print(tabulate(PRINT_Data, printHeader, tablefmt="rounded_outline",
                   colalign=("right","left","right", "right", "right",
                             "right", "right", "right", "right", "right")))

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
