#!/usr/bin/env python3

# Do this in the shell first
# ~$ mkdir my_directory
# ~$ echo "FILE" > my_directory/file.txt

from os import path

import sys

my_dir = "my_directory"
my_file = "my_directory/file.txt"
other_file = "my_directory/file2.txt"

print(f"'{my_dir}' exists: {path.exists(my_dir)}")
print(f"'{my_file}' exists: {path.exists(my_file)}")
print(f"'{other_file}' exists: {path.exists(other_file)}")
print(f"'{my_dir}' is a directory: {path.isdir(my_dir)}")
print(f"'{my_file}' is a directory: {path.isdir(my_file)}")
print(f"'{my_dir}' is a file: {path.isfile(my_dir)}")
print(f"'{my_file}' is a file: {path.isfile(my_file)}")

# End
