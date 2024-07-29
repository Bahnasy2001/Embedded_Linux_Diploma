"""
my_pyfiglet.py

This script uses the pyfiglet library to create ASCII art from a string.
In this example, the script generates an ASCII art representation of the text "Hassan Bahnasy".

Usage:
    Run the script with Python to see the output.

Requirements:
    - pyfiglet: Install using 'pip install pyfiglet'

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

# Import the pyfiglet library
import pyfiglet

# Generate ASCII art for the given text
result = pyfiglet.figlet_format("Hassan Bahnasy")

# Print the ASCII art to the console
print(result)
