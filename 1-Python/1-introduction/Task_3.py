"""
Task_3.py

This script retrieves and prints environment variables, with error handling for the specific environment variable retrieval.

Usage:
    Run the script with Python to see the output of the specific environment variable and all environment variables.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

import os

# Get a specific environment variable
username = os.getenv('USERNAME')

if username is not None:
    print(f'Username: {username}')
else:
    print('USERNAME environment variable is not set.')

# Get all environment variables
all_env_vars = os.environ
print('All Environment Variables:')
for key, value in all_env_vars.items():
    print(f"{key} : {value}")

# Explanation:
# - os.getenv('USERNAME') retrieves the value of the environment variable 'USERNAME'.
# - os.environ returns a dictionary-like object containing all environment variables.
# - We iterate over this dictionary to print each environment variable and its value.
