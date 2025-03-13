#!/usr/bin/env python3

import csv

csv_data = "data.csv"

with open(csv_data, mode="r", encoding="utf8") as fh:
    reader = csv.reader(fh)
    for row in reader:
        print(row)

header = list()
data = list()
orders_csv = "data.csv"

# // Open CSV file as a file-handle //
with open(orders_csv, mode="r", encoding="utf8") as fh:
    csv_read = list(csv.reader(fh))
    header = csv_read[0]
    data = csv_read[1:]

print(header)
print()
[print(x) for x in data]
