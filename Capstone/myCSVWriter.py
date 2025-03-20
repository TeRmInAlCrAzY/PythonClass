#!/usr/bin/env python3

import csv

data = []

data = [
    ['name', 'branch', 'year', 'CGPA'],
    ['Alan', 'waterford', '1969', '4.0'],
    ['Barry', 'bristol', '1972', '3.5'],
    ['Charles', 'cambridge', '1975', '3.0'],
    ['David', 'cambridge', '1978', '2.5'],
    ['Edward', 'cambridge', '1981', '2.0'],
    ['Frank', 'cambridge', '1984', '1.5'],
    ['George', 'cambridge', '1987', '1.0'],
    ['Harry', 'cambridge', '1990', '0.5'],
    ['Ian', 'cambridge', '1993', '0.0']
]

myName = 'George'
myBranch = 'cambridge'
myYear = '1987'
myCGPA = '1.0'

data.append([myName, myBranch, myYear, myCGPA])

myName = 'John'
myBranch = 'cambridge'
myYear = '1990'
myCGPA = '0.5'

data.append([myName, myBranch, myYear, myCGPA])

with open('university_records.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(data)