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
import csv

# ============================================ #
# //             Module imports             // #
# ============================================ #

from tools import *
import urllib.request
import json
import sys
import logging

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #


LETTERG_CSV = "letterG.csv"
LETTERK_CSV = "letterK.csv"
CSV_HEADER = ["town_code",
              "town_name",
              "pop_value",
              "males_value",
              "females_value",
              "ph_occ_value",
              "ph_unocc_value",
              "vac_dwell_value",
              "h_stock_value",
              "vac_rate_value",]

# ============================================ #
# //           getCounty Function           // #
# ============================================ #

def getCounty(town: str):
    """
    Extracts the county name from a given town string, specifically by identifying
    the occurrence of "Co." within the string, followed by processing subsequent
    characters to isolate and return the county name. If there is a comma in the
    county name, it truncates the name up to the first comma to correct the
    format.

    :param town: A string representing the town name, including the "Co."
        designation and potentially a trailing comma-separated county name.
    :type town: str

    :return: The extracted county name, trimmed and corrected of any
        extraneous trailing commas or additional text.
    :rtype: str
    """
    posCounty: int = town.find("Co.")
    county = town[posCounty+4:]
    logging.info(f"Position of Co. in {town} is {posCounty}, county is {county}")
    if county.find(",") != -1:
        logging.info("There is a comma in the county name")
        posComma = county.find(",")
        logging.info(f"The comma position is {posComma}")
        logging.info(f"The corrected county name is {county[:posComma]}")
        county=county[:posComma]

    return county

def getTown(town: str):
    posCounty: int = town.find("Co.")
    town = town[3:posCounty-1]
    return town

def main():
    """This is the main() function"""
    # Set the logging level to info
    logging.basicConfig(level=logging.INFO)

    # Pull the JSON data from the suppied url
    with urllib.request.urlopen("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CD176/JSON-stat/1.0/en") as url:
        data = json.load(url)
        logging.info(data)

    # Save the data to a json file in the current working directory called CSO.json
    outfile = open("CSO.json", "w")
    json.dump(data, outfile)
    outfile.close()
    
    # Import CSO.json to a dictionary
    infile = open("CSO.json", "r")
    data = json.load(infile)
    infile.close()

    # Build a lookup list from $.dataset.dimension.C03198V03862.category.label
    # This will allow us to look up the population data later
    lookup = {}
    for key, value in data["dataset"]["dimension"]["C03198V03862"]["category"]["label"].items():
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

    # Declare a dictionary called gTowns
    gTowns = {}
    logging.info("Building dictionary of G towns")

    # step through the list of towns in allTowns. print each key and value in allTowns
    for key, town in allTowns.items():
        # print(f"Town: {town}")
        if town[4] == "G":
            # add town to dictionary gTowns with key index
            gTowns[key] = town

    logging.info("***Dictionary of G towns")
    logging.info(gTowns)

    # So we have our list of G towns in a dictionary. We now need to step through the items in the dictionary, extract the index, use
    # that index to lookup the data in the values list

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
        males_value = values[adjusted_key+1]
        females_value = values[adjusted_key+2]
        ph_occ_value = values[adjusted_key+3]
        ph_unocc_value = values[adjusted_key+4]
        vac_dwell_value = values[adjusted_key+5]
        h_stock_value = values[adjusted_key+6]
        vac_rate_value = values[adjusted_key+7]

        CSV_Data.append(
            [key, town, pop_value, males_value, females_value, ph_occ_value, ph_unocc_value, vac_dwell_value, h_stock_value, vac_rate_value])

        #logging.info(f"Town: {town} -- Population: {pop_value}")
        print(f"{key},{town},{pop_value},{males_value},{females_value},{ph_occ_value},{ph_unocc_value},{vac_dwell_value},{h_stock_value},{vac_rate_value}")

    csv_writer = csv.writer(fh, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(CSV_Data)

    #print the type of data

    # logging.info(type(data))

    # # Output the data relating to all towns starting with the letter 'G'
    # g_towns_list = [town for town in allTowns.values() if town[4] == 'G']
    # logging.info("Towns starting with G:")
    # logging.info(g_towns_list)
    #
    # # Declare a blank list of G towns
    # g_towns_list = []
    #
    # logging.info("G towns noted")
    # for town in (g_towns.values()):
    #     logging.info(town)
    #     if town[4] == "G":
    #         logging.info("G Town!")
    #         g_towns_list.append(town)
    #
    # logging.info("G towns list")
    # for town in g_towns_list:
    #     logging.info(town)
    #     county = getCounty(town)
    #     logging.info(county)


# # For each town, find the 4th character in the string
# printHeader("4th character in town name")
# for town in (g_towns.values()):
#     print(town[3])

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
