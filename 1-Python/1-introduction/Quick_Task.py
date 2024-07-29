"""
Quick_Task.py

This script prompts the user to enter two numbers and performs basic arithmetic operations 
(addition, subtraction, multiplication, and division) on these numbers. It includes error 
handling for division by zero.

Usage:
    Run the script with Python, and follow the prompts to enter two numbers.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

# Prompt the user to enter the first number
x = int(input("Please Enter first Number: "))  # Convert the input string to an integer

# Prompt the user to enter the second number
y = int(input("Please Enter second Number: "))  # Convert the input string to an integer

# Perform and print the result of addition
print(f"Addition: {x + y}")

# Perform and print the result of subtraction
print(f"Subtraction: {x - y}")

# Perform and print the result of multiplication
print(f"Multiplication: {x * y}")

# Perform and print the result of division, handling division by zero
try:
    print(f"Division: {x / y}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
