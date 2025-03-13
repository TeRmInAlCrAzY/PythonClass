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

from tools import *
import urllib.request
import json

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
    print(f"Position of Co. in {town} is {posCounty}, county is {county}")
    if county.find(",") != -1:
        print("There is a comma in the county name")
        posComma = county.find(",")
        print(f"The comma position is {posComma}")
        print(f"The corrected county name is {county[:posComma]}")
        county=county[:posComma]

    return county


with urllib.request.urlopen("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CD176/JSON-stat/1.0/en") as url:
    data = json.load(url)
    print(data)

# save the data to a json file in the current working directory called CSO.json
with open("CSO.json", "w") as outfile:
    json.dump(data, outfile)

# import CSO.json to a dictionary
with open("CSO.json", "r") as infile:
    data = json.load(infile)

#print the type of data

printHeader("Type of Data")
print(type(data))

# Output the data relating to all towns starting with the letter 'G'
printHeader("Towns starting with G")
g_towns = data["dataset"]["dimension"]["C03198V03862"]["category"]["label"]
print(g_towns)

# Declare a blank list of G towns
g_towns_list = []

printHeader("G towns noted")
for town in (g_towns.values()):
    print(town)
    if town[4] == "G":
        print("G Town!")
        g_towns_list.append(town)

printHeader("G towns list")
for town in g_towns_list:
    print(town)
    county = getCounty(town)
    print (county)


# # For each town, find the 4th character in the string
# printHeader("4th character in town name")
# for town in (g_towns.values()):
#     print(town[3])

