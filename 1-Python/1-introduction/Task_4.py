"""
Task_4.py

This script calculates and prints the area of a circle based on the radius provided by the user.

Usage:
    Run the script with Python. Enter the radius when prompted to receive the area of the circle.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

import math

# Prompt the user to enter the radius of the circle
radius = float(input("Enter radius: "))

# Calculate the area of the circle using the formula: Area = π * radius^2
area = math.pi * radius * radius

# Print the calculated area
print(f"Area = {area:.2f}")

# Explanation:
# - We use the math.pi constant to get the value of π.
# - The formula for the area of a circle is π * radius^2.
# - The result is printed with two decimal places for better readability.
