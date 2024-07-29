"""
Task_1.py

This script counts the number of occurrences of the number 4 in a given list.

Usage:
    Run the script with Python. The script will print the count of the number 4 in the predefined list.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

# Define the list of numbers
my_list = [1, 4, 5, 6, 7, 4]

# Initialize a counter to zero
count = 0

# Iterate over each element in the list
for x in my_list:
    if x == 4:
        # Increment the counter if the element is 4
        count += 1
    else:
        # Optional: pass statement is redundant here but shown for completeness
        pass

# Print the final count of the number 4
print(count)
