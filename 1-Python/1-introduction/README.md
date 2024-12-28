# Python Scripts Documentation 📜🐍

 ![Static Badge](https://img.shields.io/badge/python-3.12.3-yellow?logo=python&logoColor=blue) ![Static Badge](https://img.shields.io/badge/Embedded%20Linux%20-Diploma-green?logo=Linux&logoColor=blue)

## Overview 🌟

This repository contains several Python scripts demonstrating different functionalities. Below are descriptions and usage instructions for each script.

## Scripts 📂

### 1. **my_pyfiglet.py** 🎨

This script uses the `pyfiglet` library to create ASCII art from a string. In this example, the script generates an ASCII art representation of the text "Hassan Bahnasy".

#### Usage 🚀

1. Run the script with Python.
2. The script will print ASCII art of the text "Hassan Bahnasy".

#### Requirements 📦

- `pyfiglet`: Install using `pip install pyfiglet`

#### Example Code 📝

```python
import pyfiglet

result = pyfiglet.figlet_format("Hassan Bahnasy")
print(result)
```

### 2. **Quick_Task.py** ➕➖✖️➗

This script prompts the user to enter two numbers and performs basic arithmetic operations (addition, subtraction, multiplication, and division) on these numbers. It includes error handling for division by zero.

#### Usage 🚀

1. Run the script with Python.
2. Enter two numbers when prompted.

#### Example Code 📝

```python
x = int(input("Please Enter first Number: "))
y = int(input("Please Enter second Number: "))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

### 3. **Quick_Task2.py** 🔑

This script authenticates a user based on a provided username and password. It checks if the username exists in a predefined dictionary and if the provided password matches the stored password for that username. Includes basic error handling.

#### Usage 🚀

1. Run the script with Python.
2. Enter a username and password when prompted.

#### Example Code 📝

```python
passDict = {
    "Ahmed": 1394,
    "Ali": 6078,
    "Amr": 9354
}

def authentication(username, password):
    if username in passDict:
        if int(password) == passDict[username]:
            return True
    return False

username = input("Please enter your username\n").capitalize()
password = input("Please enter your password\n")

if authentication(username, password):
    print(f"Welcome, {username}!\n")
else:
    print("Incorrect username or password!\n")
```

### 4. **Task_1.py** 🔢

This script counts the number of occurrences of the number 4 in a given list.

#### Usage 🚀

1. Run the script with Python.
2. The script will print the count of the number 4 in the predefined list.

#### Example Code 📝

```python
my_list = [1, 4, 5, 6, 7, 4]

count = 0

for x in my_list:
    if x == 4:
        count += 1
    else:
        pass

print(count)
```

### 5. **Task_2.py** 💡

This script checks whether a provided character is a vowel or not. It handles both uppercase and lowercase inputs.

#### Usage 🚀

1. Run the script with Python.
2. Enter a character when prompted.

#### Example Code 📝

```python
vowel = ['a', 'e', 'i', 'o', 'u']

x = input("Enter a Character:")

if x.lower() in vowel:
    print(f"{x} is a vowel")
else:
    print(f"{x} is not a vowel")
```

### 6. **Task_3.py** 🖥️

This script retrieves and prints environment variables, with error handling for the specific environment variable retrieval.

#### Usage 🚀

1. Run the script with Python.
2. The script will print the value of the `USERNAME` environment variable and all environment variables.

#### Example Code 📝

```python
import os

# Get a specific environment variable
username = os.getenv('USERNAME')
print(f'Username: {username}')

# Get all environment variables
all_env_vars = os.environ
print('All Environment Variables:')
for key, value in all_env_vars.items():
    print(f"{key} : {value}")
```

### 7. **Task_4.py** ⚪

This script calculates and prints the area of a circle based on the radius provided by the user.

#### Usage 🚀

1. Run the script with Python.
2. Enter the radius when prompted to receive the area of the circle.

#### Example Code 📝

```python
import math

# Prompt the user to enter the radius of the circle
radius = float(input("Enter radius: "))

# Calculate the area of the circle using the formula: Area = π * radius^2
area = math.pi * radius * radius

# Print the calculated area
print(f"Area = {area:.2f}")
```

### 8. **Task_5.py** 📅

This script prints the calendar for a specified month and year using Python's `calendar` module.

#### Usage 🚀

1. Run the script with Python.
2. Enter the desired month and year when prompted to see the calendar for that month.

#### Example Code 📝

```python
import calendar

# Prompt the user to enter the month and year
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

# Display the calendar for the specified month and year
print(calendar.month(year, month))
```

## Author 👤

**Hassan Ahmed Fathy, El Bahnasy**  
- [LinkedIn](https://www.linkedin.com/in/hassanbahnasy/)  
- [GitHub](https://github.com/Bahnasy2001)  
- Contact: hassanbahnasy872@gmail.com