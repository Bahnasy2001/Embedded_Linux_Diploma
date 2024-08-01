import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time
print("Current date and time: ")

# Format and print the date and time, removing the last 7 characters
# (usually to exclude microseconds)
print(str(now)[0:-7])
