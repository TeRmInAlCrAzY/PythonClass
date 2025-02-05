#!/usr/bin/env python3

"""
Title: Pinger.py - Exercise program to ping a remote host and check connectivity
Author: Alan MacDonald
Date: 05/02/2025

This program asks the user to input an IP address and then runs a ping command
to check connectivity. It then outputs whether the IP address is reachable or
unreachable based on the result of the ping command.

Observations:
- The program does not handle any exceptions that may occur during execution.
- The program does not check if the provided IP address is valid.
- The code that would display if the ip is not valid will never execute as in this case the program crashes.
- The program is written to work with Linux systems only.
- A commented line is included with the windows equivalent
"""

import subprocess as sp

# Ask the user for an IP address to test
ip_address = input("Enter an IP address to test connectivity: ")
print(f"Testing connectivity to {ip_address} ...")

# Run the PING command and return the result in response
response = sp.run(["ping", "-c", "1", ip_address], stdout=sp.PIPE, check=True)
# Windows version
# response = sp.run(["ping", "-n", "1", ip_address], stdout=sp.PIPE, check=True)      # Windows version
print(f"The response return code is {response.returncode}.")

# Check the return code
if response.returncode == 0:
    print(f"The IP address {ip_address} is alive.")
else:
    # this code never executes as program crashes due to unhandled exception
    # Included just to be complete
    print(f"The IP address {ip_address} is unreachable.")


