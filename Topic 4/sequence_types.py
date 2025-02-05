#!#!/usr/bin/env python3

"""
Title: Sequence Types in Python3
Author: Alan MacDonald
Date: 05/02/2025

This program demonstrates the use of sequence types in Python3.

Observations:
- I did not have the contacts to make the classmates dictionary so I made up some data.
"""

# Declare a dictionary called dict_
dict_ = {}

# create a list called list_ of all the letters in the English alphabet
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Loop through the list_ and assign to the dictionary
for count in range(len(list_)):
    dict_[list_[count]] = count + 1

# Show the type of the variable dict_, and it's contents
print(f"The type of _dict is {type(dict_)}")
print(f"The contents of _dict are\n{dict_}")

# Declare a tuple called tuple_
tuple_ = ()

# Copy the contents of the list list_ into tuple_
tuple_ = tuple(list_)

# Show the type of the variable tuple_, and it's contents
print(f"The type of tuple_ is {type(tuple_)}")
print(f"The contents of tuple_ are\n{tuple_}")

# Extend the list list_ with the list 'A','B','C'
list_.extend(['A', 'B', 'C'])

# Show the type of the variable list_, and it's contents
print(f"The type of list_ after extending is {type(list_)}")
print(f"The contents of list_ after extending is\n{list_}")

# Convert all elements in list_ to lowercase using comprehension
list_ = [x.lower() for x in list_]

# Show the type of the variable list_, and it's contents
print(f"The type of list_ after converting to lowercase is {type(list_)}")
print(f"The contents of list_ after converting to lowercase is\n{list_}")

list2_ = []

# Create a new list, list2_, from the keys in the dictionary dict_
for key in dict_:
    list2_.append(key)

# Show the type of the variable list2_, and it's contents
print(f"The type of list2_ is {type(list2_)}")
print(f"The contents of list2_ is\n{list2_}")

# Is list2_ a subset of list_
if set(list2_).issubset(set(list_)):
    print("list2_ is a subset of list_")
else:
    print("list2_ is not a subset of list_")

# print the keys in dict_ separated by _ symbol
print(*dict_, sep="_")

classmates_ = {}

classmates_['Alan'] = 'Pottery for Cats'
classmates_['Aisling'] = 'Flower Arranging'
classmates_['Dmytro'] = 'Painting by Numbers'
classmates_['Pawel'] = 'Gardening'
classmates_['Tamzene'] = 'Extreme Ironing'
classmates_['Wadeh'] = 'Zen Motorcycle Maintenance'

# Show the type of the variable classmates, and it's contents
print(f"The type of classmates is {type(classmates_)}")
print(f"The contents of classmates are\n{classmates_}")