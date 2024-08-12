# Labs Scripts

## Overview

The `Labs` subfolder within `4-advanced_Cont` includes scripts that showcase advanced Python techniques and features. The focus is on demonstrating and experimenting with class structures, inheritance, operator overloading, and file handling.

Within the `Labs` subfolder, there are several specialized folders:

- `csv`: Contains scripts for handling CSV files.
- `EXCEL_Python_Tasks`: Contains scripts for working with Excel files using Python.
- `threading`: contains Python scripts that demonstrate the use of the `threading` module to manage and execute concurrent tasks. These scripts explore creating, starting, and managing threads, as well as printing information related to threads and processes.


### 1. **Class.py**

This script demonstrates several advanced Python concepts related to class definitions, private members, and property decorators.

#### Description

- **Encapsulation**: The script shows how to use private variables and methods in Python. It demonstrates name mangling to access private members and methods.
- **Property Decorators**: The script illustrates the use of `@property`, `@<property_name>.setter`, and `@<property_name>.deleter` decorators to manage private variables.

#### Example Code

```python
class test:
    __m = 10

    def printm(self):
        print(self.__m)

    def __pvfun(self):
        print("hello")

t = test() 
t.printm() # Print 10
#print(t.__m) #ERROR
print(t._test__m) #WORKS # Print 10
t._test__pvfun() #WORKS # Print hello

class MyClass:
    def __init__(self):
        self.__private_variable = 10  # Private member

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

obj = MyClass()
print(obj.get_private_variable())  # Accessing private member
obj.set_private_variable(20)  # Modifying private member
print(obj.get_private_variable())  # Accessing modified private member

class Student:
    name = "unknown"

    def __init__(self):
        self.age = 20
        self._my_variable = 10

    @staticmethod
    def tostring():
        print('student class')
    @property
    def my_variable(self):
        return self._my_variable

    @my_variable.setter
    def my_variable(self, value):
        self._my_variable = value

    @my_variable.deleter
    def my_variable(self):
        del self._my_variable

print(Student.tostring()) # Print None if it does not return anything 
obj = Student()

# Accessing the property like an attribute
print(obj.my_variable)

# Setting the property
obj.my_variable = 20

# Deleting the property
del obj.my_variable
```

#### Usage 

1. Place the `class.py` script inside the `Labs` folder within `4-advanced_Cont`.
2. Run the script with Python to observe the output and behavior of private members and property decorators.

### 2. **operator.py**

This script demonstrates the overloading of the `+` operator in Python classes to perform addition on custom objects.

#### Description

Operator Overloading: The script shows how to overload the `+` operator to enable the addition of two `Point` objects, resulting in a new `Point` object with the summed coordinates.

#### Example Code

```python
class Point:

    def __init__(self, xCoord=0, yCoord=0):
        self.xCoord = xCoord
        self.yCoord = yCoord

    # Overload + operator
    def __add__(self, point_ov):
        return Point(self.xCoord + point_ov.xCoord, self.yCoord + point_ov.yCoord)
    
point1 = Point(2, 4)
point2 = Point(12, 8)
point3 = point1 + point2
print(point3.xCoord)
```

#### Usage

1. Place the `operator.py` script inside the `Labs` folder within `4-advanced_Cont`.
2. Run the script with Python to observe the result of adding two `Point` objects.

### 3. **course.py**

This script demonstrates advanced class features such as constructors, destructors, inheritance, and method overriding.

#### Description

- **Constructors and Destructors**: Shows how to define and use constructors and destructors in Python classes.
- **Inheritance**: Demonstrates how to inherit from a base class and override methods in the derived class.

#### Example Code 

```python
class Person:
    '''
    Hassan Bahnasy
    '''
    name = ""

    def __init__(self, name):
        print("Constructor is called")
        print(self)
        self.name = name
        print(self.name)

    def greeting(self):
        print("Hello")

    def __str__(self):
        return ("Description of Class Person")

    def __del__(self):
        print("Destructor is called")

Hassan = Person("Hassan")
Hassan.greeting()
print(Hassan)
print(Hassan.__doc__)


class animal:
    name = ""
    def __init__(self, name):
        print("1Constructor is called")
        self.name = name

    def eat(self):
        print("eat food")

    def __del__(self):
        print("1Destructor is called")

class cat(animal):
    def __init__(self, name):
        print("2Constructor is called")
        super().__init__(name)

    def sound(self):
        print("Meaouu")

    def __del__(self):
        print("2Destructor is called")
        super().__del__()

mycat = cat("hera")
mycat.eat()
mycat.sound()
```

#### Usage
1. Place the `course.py` script inside the `Labs` folder within `4-advanced_Cont`.
2. Run the script with Python to observe class behaviors, including constructors, destructors, and inheritance.

### 4. **Quick_Task.py**

This script compares two different methods of calculating the number of lines in a file: a straightforward method using file reading and a more "C-style" method using enumeration.

#### Description
- **Python Style**: Reads the entire file into a list and prints the number of lines.
- **C Style**: Uses enumeration to count lines while iterating through the file.

#### Example Code

```python
# Python style
f = open("demofile2.txt", "r")
lst = f.readlines()
print(len(lst))

# C style
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print("Number of lines in the file: ", file_lengthy("demofile2.txt"))
```

#### Usage 

Usage
1. Place the `Quick_Task.py` script inside the `Labs` folder within `4-advanced_Cont`.
2. Ensure that the file `demofile2.txt` is present in the same directory as the script.
3. Run the script with Python to see the number of lines printed using both methods.

### 5. **Quick_Task2.py**

This script compares two different methods of calculating the number of words in a file: a straightforward method using file reading and a more "C-style" method using file reading and splitting.

#### Description
- **Python Style**: Reads the entire file and counts the number of words by splitting the content.
- **C Style**: Reads the file and counts words by splitting the content after reading.

#### Example Code

```python
# Python style
f = open("demofile2.txt", "r")
st = f.read()
print(len(st.split()))

# C style
def word_count(fname):
    with open(fname) as f:
        return (f.read().split())
    
print("Number of Words: ", len(word_count("demofile2.txt")))
```

#### Usage

1. Place the `Quick_Task2.py` script inside the `Labs` folder within `4-advanced_Cont`.
2. Ensure that the file `demofile2.txt` is present in the same directory as the script.
3. Run the script with Python to see the number of words counted using both methods.


### 6. **Quick_Task3.py**

This script demonstrates how to append a list of colors to an existing file and then read the updated content.

#### Description

- **File Appending and Reading**: Shows how to append a list of colors to a file and read the updated file content.

#### Example Code

```python
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('demofile2.txt', 'a') as myfile:
    myfile.write(" ".join(color))

content = open('demofile2.txt')
print(content.read())
```

#### Usage

1. Place the `Quick_Task3.py` script inside the `Labs` folder within `4-advanced_Cont`.
2. Ensure that the file `demofile2.txt` is present in the same directory as the script.
3. Run the script with Python to see the updated content of the file after appending the list of colors.

### 7. **my_csv_test.py** (in the `csv` folder)

This script demonstrates how to create and write data to a CSV file using Python's `csv` module.

#### Description

- **CSV Writing**: Shows how to open a CSV file and write data to it using the `csv` module.

#### Code

```python
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
```

#### Usage

1. Place the `my_csv_test.py` script inside the `csv` folder within `Labs`.
2. Run the script with Python to create and write data to `output.csv`.

### 8. **my_csv_test2.py** (in the `csv` folder)

This script demonstrates how to read data from a CSV file and store it in a dictionary. It also prints the content of the CSV file and the dictionary representation.

#### Description
- **CSV Reading and Dictionary Storage**: Shows how to read a CSV file and store its contents in a dictionary with the first column as the key and the remaining columns as the values.
- **Printing CSV Content**: Prints each line from the CSV file and the final dictionary.

#### Example Code 

```python
import csv

reader = csv.reader(open('output.csv', 'r'))
mydict = {}
for line in reader:
    mydict[line[0]] = {line[1], line[2]}
    
    print('\t'.join(line))

print(mydict)
```

#### Usage

1. Place the `my_csv_test2.py` script inside the `csv` folder within `Labs`.
2. Run the script with Python to read and print the contents of `output.csv` and display the dictionary representation.

### 9. **Test.py** (in the `EXCEL_Python_Tasks` folder)

This script demonstrates how to create and write data to an Excel file using the `openpyxl` library.

#### Description
- **Excel Writing**: Shows how to create a new Excel workbook, write data to cells, and save the workbook.

#### Example Code 

```python
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
worksheet.append(['Hassan', 22])

# Save the workbook
workbook.save('Test.xlsx')
```

#### Usage

1. Place the `test.py` script inside the `EXCEL_Python_Tasks` folder within `Labs`.
2. Run the script with Python to create and save an Excel file named `Test.xlsx`.

### 10. **Test2.py** (in the `EXCEL_Python_Tasks` folder)

This script demonstrates how to read data from an Excel file and access its contents using the `openpyxl` library.

#### Description

- **Excel Reading**: Shows how to load an existing Excel workbook, access cell values, and iterate over rows and columns to print their contents.

#### Example Code

```python
from openpyxl import load_workbook

# Load the Excel file
workbook = load_workbook('Test.xlsx')

# Select the active worksheet
worksheet = workbook.active

# Access cell values
print(worksheet['A1'].value)  # Print value of cell A1
print(worksheet.cell(row=2, column=2).value)  # Print value of cell B2

# Iterate over rows and columns
for row in worksheet.iter_rows(min_row=1, max_row=4, min_col=1, max_col=2):
    for cell in row:
        print(cell.value, end='\t')
    print()  # Move to the next line
```

#### Usage

1. Place the `Test2.py` script inside the `EXCEL_Python_Tasks` folder within `Labs`.
2. Run the script with Python to read and print the contents of the `Test.xlsx` Excel file.

### 11. **Test3.py** (in the `EXCEL_Python_Tasks` folder)

This script demonstrates how to style cells in an Excel file using the `openpyxl` library. It also updates an existing Excel file with new styles.

#### Description

- **Styling Cells**: Shows how to apply styling such as font and alignment to cells in an Excel workbook. It updates both a new workbook and an existing one.

#### Example Code 

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment

# Create a new Workbook
workbook = Workbook()

# Load the Excel file
workbook2 = load_workbook('Test.xlsx')

# Create a new WorkSheet
worksheet = workbook.active
worksheet2 = workbook2.active

# Write data to cells
worksheet['A1'] = 'Bold and Centered'
worksheet['A1'].font = Font(bold=True)
worksheet['A1'].alignment = Alignment(horizontal='center')

worksheet2['A1'].font = Font(bold=True)
worksheet2['A1'].alignment = Alignment(horizontal='center')

# Save the workbook
workbook.save('styled_output.xlsx')
# Save the workbook
workbook2.save('Test.xlsx')
```

#### Usage

1. Place the `Test3.py` script inside the `EXCEL_Python_Tasks` folder within `Labs`.
2. Run the script with Python to apply styling to cells in both a new Excel file (`styled_output.xlsx`) and an existing Excel file (`Test.xlsx`).

### 12. **Lab.py** (in the `threading` folder)

This script demonstrates basic threading by creating and running two threads concurrently. Each thread executes a simple task function that prints a message multiple times.

#### Description

- **Thread Creation**: Shows how to create and start threads using the `threading.Thread` class.
- **Thread Execution**: Demonstrates running two threads in parallel and waiting for both to complete using `join()`.

#### Code

```python
#import the threading module
import threading

def task1(num):
    for i in range(0,num):
        print('task1')

def task2(num):
    for i in range(0,num):
        print('task2')

if __name__ == "__main__":
    #creating threads
    t1 = threading.Thread(target=task1,args=(5,))
    t2 = threading.Thread(target=task2,args=(5,))

    #starting thread 1
    t1.start()
    #starting thread 2
    t2.start()
    #wait until thread 1 is completely executed
    t1.join()
    #wait until thread 2 is completely executed
    t2.join()

    #both threads are completely executed
    print('Done!')
```

#### Usage

1. Place the `Lab.py` script inside the `threading` folder within `Labs`.
2. Run the script with Python to see how threads execute concurrently and print their messages.

#### Output

The script will print 'task1' and 'task2' messages from two different threads and then print 'Done!' after both threads have completed execution.

### 13. **Lab2.py** (in the `threading` folder)

This script provides a more detailed example of threading, including printing the names of threads and process IDs. It demonstrates how to identify the thread and process running each task.

#### Description

- **Thread and Process Information**: Shows how to print the thread name and process ID for each task to understand which thread and process are executing the code.
- **Main Thread Information**: Prints information about the main thread and process ID before creating and starting new threads.

#### Example Code 
```python
#import the threading module
import threading
import os

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    #print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    #print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    #creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')


    # starting threads
    t1.start()
    t2.start()
```

#### Usage

1. Place the `Lab2.py` script inside the `threading` folder within `Labs`.
2. Run the script with Python to see the thread and process information printed for each task.

#### Output

The script will print the names of the threads, the process ID for each task, and the process ID and main thread name of the main program.

---

# Tasks Scripts

## Overview

This folder contains scripts and utilities for various tasks related to embedded systems and programming. Below is an overview of the contents and functionality of each script within the `Tasks` folder.

### 1. **Task_1.py** (in the `Task_1` folder)

This script is designed to generate an initialization function for GPIO (General Purpose Input/Output) configuration in AVR microcontrollers. The script writes to a C file, `init.c`, which includes a function to set the direction of the PORTA pins based on user input. The user is prompted to specify the mode (input or output) for each of the 8 bits of the PORTA register.

#### Key Features

- Prompts the user to input the mode for each bit (input or output).
- Generates a C function that configures the PORTA register based on the user’s input.
- Writes the generated function to the `init.c` file in the format suitable for AVR microcontroller initialization.

#### Usage

1. Run the script in a Python environment.
2. Input the mode for each bit when prompted.
3. The script will generate the `init.c` file with the appropriate initialization function.

#### Example Output

```C
void init_PORTA_DIR (void)
{
    DDRA = 0b00001111;
}
```

The above example shows a generated function where the first four bits are set as output (`1`) and the remaining four bits are set as input (`0`).


### 2. **Check_Email.py** (in the `Task_2` folder)

This script automates the process of checking unread emails in Gmail and marking them as read. It uses the `pyautogui` library to interact with the email application or web browser.

#### Key Features
- Opens Gmail in the Brave browser.
- Navigates to the inbox and locates the first unread email.
- Marks the first unread email as read.

#### Usage
1. Make sure the pyautogui and webbrowser libraries are installed.
2. Customize the coordinates for your specific email application or web browser setup.
3. Run the script in a Python environment

#### Important Notes
- Adjust the sleep times (`time.sleep()`) if necessary to match the loading times of your email application or web browser.
- Customize the coordinates for interacting with UI elements based on your setup:
    - `first_unread_email` coordinates: Position of the first unread email in the inbox.
    - `mark_as_read_button` coordinates: Position of the "Mark as Read" button.

### 3. **Battery_Status.py** (in the `Task_2` folder)

This script monitors the battery status of the system and sends a desktop notification with the current battery percentage. It uses the `psutil` library to check the battery status and the `plyer` library to send notifications

#### Key Features

- Checks the battery percentage using `psutil`.
- Sends a desktop notification displaying the battery percentage.

#### Usage

1. Make sure the `psutil` and `plyer` libraries are installed.
2. Run the script in a Python environment to get a notification about the current battery status.

#### Important Notes

- The notification will display the battery percentage and remain visible for 10 seconds (`timeout=10`).

### 4. **command_line_args.py** (in the `Task_2` folder)

This script demonstrates how to handle command-line arguments in Python. It prints out all command-line arguments provided to the script.

#### Key Features

- Checks if command-line arguments are provided.
- Prints all command-line arguments with their indices.

#### Usage
1. Run the script with command-line arguments to see them printed in the console
```sh
python command_line_args.py arg1 arg2 arg3
```

### 5. **get_ascii.py** (in the `Task_2` folder)

This script retrieves and prints the ASCII value of a single character input by the user. It ensures that the input is a single character and raises an error if it is not.

#### Key Features

- Prompts the user to enter a single character.
- Retrieves and prints the ASCII value of the character using the `ord()` function.
- Handles errors if the input is not a single character.

#### Usage

1. Run the script and input a single character when prompted.
2. The script will display the ASCII value of the entered character.

### 6. **parse_header_to_excel.py** (in the `Task_2` folder)

This script parses a C header file to extract function prototypes and writes them to an Excel file. It uses regular expressions to find function prototypes and the `pandas` library to create and save an Excel file.

#### Key Features

- Parses a header file to extract function prototypes using regular expressions.
- Writes the extracted prototypes to an Excel file using `pandas` and `openpyxl`.

#### Usage

1. Ensure `pandas` and `openpyxl` libraries are installed.
2. Run the script and provide the path to the header file and the desired output Excel file path.
```sh
python parse_header_to_excel.py
```

#### Example Output

- The output file, `function_prototypes.xlsx`, will contain LCD function prototypes extracted from the provided header file.

### 7. **Google_Assistant.py** (in the `Task_3` folder)

This script creates a virtual assistant that interacts in English, using text-to-speech (gTTS) and speech recognition (speech_recognition). It performs tasks such as:

- Greeting the user.
- Providing the current time and date.
- Searching Google based on user input.
- Finding locations using Google Maps.
- Opening GitHub and LinkedIn profiles.
- Exiting the assistant based on user command.

#### Dependencies

- `webbrowser`
- `playsound`
- `gtts`
- `speech_recognition`
- `datetime`

#### Usage

1. Run the script using python `Google_Assistant.py`.
2. Follow voice prompts to interact with the assistant.

### 8. **Google_Assistant_Arabic.py** (in the `Task_3` folder)

This script creates a virtual assistant that interacts in Arabic, using text-to-speech (gTTS) and speech recognition (speech_recognition). It includes similar functionalities to the English assistant but in Arabic. Tasks include:

- Greeting the user in Arabic.
- Providing the current time and date in Arabic.
- Searching Google in Arabic.
- Finding locations using Google Maps in Arabic.
- Opening GitHub and LinkedIn profiles in Arabic.
- Exiting the assistant based on user command.

#### Dependencies

- `webbrowser`
- `playsound`
- `gtts`
- `speech_recognition`
- `datetime`

#### Usage

1. Run the script using python `Google_Assistant_Arabic.py`.
2. Follow voice prompts to interact with the assistant in Arabic.