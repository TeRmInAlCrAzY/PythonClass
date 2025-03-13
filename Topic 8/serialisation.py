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
import tools
from pprint import pprint

from Capstone.tools import printHeader

YAML_FILE = "network.yaml"
JSON_FILE = "network.json"

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
print(f"The type of the data is {type(data)}")
printHeader("The contents of the data")
print(data)
print(f"{data.get('network').get('ethernets').get('ens192').get('addresses')}")
mystring=str(data.get('network').get('ethernets').get('ens192').get('addresses'))


print(f"The type of the string is {type(mystring)}")
print(f"The string is {mystring}")
print(f"The string is {mystring[2:-2]}")

fh.close()