#! /usr/bin/env python3
""" CSV Write """

import csv

header = ["name", "model", "year"]
data = [
["toyota", "corolla", "2016"],
["ford", "escort", "2016"],
["nissan", "yaris", "2019"],
["seat", "leon", "2020"],
["volvo", "xc60", "2021"],
]
cars_csv = "cars.csv"

# // Open CSV file as a file-handle //
with open(cars_csv, mode="w", encoding="utf8") as fh:
    writer = csv.writer(fh)
    writer.writerow(header)
    writer.writerows(data)

#