"""
Quick_Task2.py

This script authenticates a user based on a provided username and password. 
It checks if the username exists in a predefined dictionary and if the provided 
password matches the stored password for that username. Includes basic error handling.

Usage:
    Run the script with Python, and follow the prompts to enter a username and password.

Author:
    Hassan Ahmed Fathy El Bahnasy
"""

# Dictionary storing usernames and their corresponding passwords
passDict = {
    "Ahmed": 1394,
    "Ali": 6078,
    "Amr": 9354
}

def authentication(username: str, password: str) -> bool:
    """
    Authenticate a user by checking the username and password.

    Parameters:
    - username (str): The username to authenticate.
    - password (str): The password provided by the user.

    Returns:
    - bool: True if authentication is successful, False otherwise.
    """
    if username in passDict:
        try:
            # Check if the provided password matches the stored password
            if int(password) == passDict[username]:
                return True
        except ValueError:
            # Handle the case where password is not an integer
            print("Error: Password must be a numeric value.")
    return False

# Prompt the user to enter their username
username = input("Please enter your username\n").capitalize()

# Prompt the user to enter their password
password = input("Please enter your password\n")

# Authenticate the user and display an appropriate message
if authentication(username, password):
    print(f"Welcome, {username}!\n")
else:
    print("Incorrect username or password!\n")
