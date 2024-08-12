import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write each row of data to the CSV file
    for row in data:
        writer.writerow(row)
