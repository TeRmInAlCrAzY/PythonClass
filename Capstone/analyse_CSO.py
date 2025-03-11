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
print(type(data))

# Output the data relating to all towns starting with the letter 'G'

