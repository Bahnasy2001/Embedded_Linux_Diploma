"""
Task_5.py

This script prints the calendar for a specified month and year using Python's calendar module.

Usage:
    Run the script with Python. Enter the desired month and year when prompted to see the calendar for that month.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

import calendar

# Prompt the user to enter the month and year
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

# Display the calendar for the specified month and year
print(calendar.month(year, month))

# Explanation:
# - The calendar.month(year, month) function returns a multi-line string representing the calendar for the specified month and year.
# - The user is prompted to enter the month and year, which are then used to generate and print the calendar.
