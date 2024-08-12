#Writing Data to an Excel File:
from openpyxl import Workbook
# Create a new workbook
workbook = Workbook()

# Create a new worksheet
worksheet = workbook.active

# Write data to cells
worksheet['A1'] = 'Name'
worksheet['B1'] = 'Age'
worksheet.append(['John', 30])
worksheet.append(['Alice', 25])
worksheet.append(['Hassan',22])

# Save the workbook
workbook.save('Test.xlsx')
