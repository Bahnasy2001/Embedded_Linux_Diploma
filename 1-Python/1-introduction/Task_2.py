"""
Task_2.py

This script checks whether a provided character is a vowel or not. 
It handles both uppercase and lowercase inputs.

Usage:
    Run the script with Python, and follow the prompt to enter a character.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Prompt the user to enter a character
x = input("Enter a character: ")

# Check if the entered character is a single letter
if len(x) == 1 and x.isalpha():
    # Convert the character to lowercase and check if it's in the vowels list
    if x.lower() in vowels:
        print(f"{x} is a vowel")
    else:
        print(f"{x} is not a vowel")
else:
    print("Invalid input. Please enter a single letter.")
