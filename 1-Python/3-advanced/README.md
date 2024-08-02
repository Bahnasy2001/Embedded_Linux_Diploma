# Task 1 Scripts

## Overview

This folder contains Python scripts related to Task 1, including `Task_1.py` and `firelink.py`. These scripts demonstrate how to interact with web pages using Python.

## Scripts

### 1. Task_1.py

This script provides a menu for users to choose between opening different social media pages in the Brave browser. The available options are Facebook, LinkedIn, and Twitter.

#### Usage

1. Run the script with Python.
2. Choose an option by entering the corresponding index (1 for Facebook, 2 for LinkedIn, 3 for Twitter).
3. The script will open the selected page in the Brave browser.

#### Example Code

```python
import firelink

print("Choose from the following options:")
print("1-Facebook Page\n2-Linkedin Page\n3-Twitter Page")
index = int(input("Choose with index:"))

firelink.firelink(index)
```

### 2. firelink.py

This script contains a function `firelink(index)` that opens a specified social media page in the Brave browser based on the provided index. The supported pages are Facebook, LinkedIn, and Twitter.

#### Usage
1. Ensure that Brave browser is installed on your system.
2. The script is used by calling the `firelink(index)` function with the desired index.

#### Example Code

```python
import webbrowser

def firelink(index):
    links = [
        "https://www.facebook.com/profile.php?id=100009364682555",
        "https://www.linkedin.com/in/hassan-bahnasy-7b4952253/",
        "https://twitter.com/bahnasy2001"
    ]
    webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open(links[index-1])
```
#### Requirements
- Brave Browser: Ensure that the Brave browser is installed in the specified path.
- webbrowser: This is a standard Python library, so no additional installation is needed.

---

# Task 2 Scripts

## Overview

This folder contains Python scripts related to Task 2. The scripts demonstrate how to interact with web APIs to retrieve information or suggestions.

## Scripts

### 1. get_public_IP.py

This script retrieves and prints the public IP address of the user's machine by sending a GET request to the ipify API.

#### Usage

1. Run the script with Python.
2. The script will print the public IP address of your machine.

#### Example Code

```python
import requests

def get_public_IP():
    try:
        # Send GET request to the ipify URL
        response = requests.get("https://api.ipify.org/?format=json")
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            #parse JSON response
            data = response.json()
            ip_address = data.get('ip')
            if ip_address:
                print("Your public IP address is:", ip_address)
            else:
                print("Failed to retrieve public IP address.")
        else:
            print("Failed to retrieve public IP address. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

get_public_IP()
```

#### Requirements
- `requests`: Install using `pip install requests`

---

### 2. suggest_activity.py

This script provides an activity suggestion by sending a GET request to the Bored API. The script retrieves a suggestion for an activity and prints it.

#### Usage
1. Run the script with Python.
2. The script will print a suggested activity for you to try.

#### Example Code

```python
import requests

def suggest_activity():
    try:
        #send GET request to the boredapi URL
        response = requests.get("https://www.boredapi.com/api/activity")
        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            #parse JSON response
            data = response.json()
            activity = data.get('activity')
            if activity:
                print("Here's an activity suggestion for you:", activity)
            else:
                print("No activity suggestion available.")
        else:
            print("Failed to retrieve activity suggestion. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred: ",e )

suggest_activity()
```

#### Requirements
- `requests`: Install using `pip install requests`

---

# Task 3 Scripts

## Overview

This folder contains Python scripts related to Task 3. These scripts automate various tasks using Python's `pyautogui` library to interact with the graphical user interface.

## Scripts

### vscode.py

This script automates the process of opening Visual Studio Code and installing several extensions using the `pyautogui` library. It performs the following actions:

1. Opens Visual Studio Code by simulating keypresses.
2. Installs the following extensions:
   - Clangd
   - C++ TestMate
   - C++ Helper
   - CMake
   - CMake Tools

#### Usage

1. Run the script with Python.
2. The script will open Visual Studio Code and sequentially install the specified extensions.

#### Example Code

```python
import time
import pyautogui

def open_vscode_and_install_extensions():
    # Open Visual Studio Code
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('visual studio code')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the delay based on your system's speed
    
    # Install clangd extension
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('clangd')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the delay based on your system's speed

    # Install C++ TestMate extension
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('C++ TestMate')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the delay based on your system's speed

    # Install C++ Helper extension
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('C++ Helper')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the delay based on your system's speed

    # Install CMake extension
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('CMake')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the delay based on your system's speed

    # Install CMake Tools extension
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('CMake Tools')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the delay based on your system's speed

open_vscode_and_install_extensions()
```

#### Requirements
- `pyautogui`: Install using pip install `pyautogui`

#### Notes
- Ensure that Visual Studio Code is installed on your system before running this script.
- Adjust the `time.sleep()` values as needed based on your system's performance to ensure that each action completes before the next one starts.

---
# Another Scripts

## Scripts

### pyautoGui.py

This script automates the process of opening the Brave browser, navigating to a specific URL, and interacting with elements on the screen using the `pyautogui` library. The script performs the following actions:

1. Opens the Brave browser.
2. Navigates to a specified URL.
3. Locates an image on the screen and performs a click action.

#### Usage

1. Run the script with Python.
2. The script will:
   - Open the Brave browser.
   - Navigate to a specified Coursera course link.
   - Locate an image on the screen and perform a click action.

#### Example Code

```python
import pyautogui
import time
import webbrowser
import os

pyautogui.hotkey('win')
pyautogui.typewrite("brave")
pyautogui.hotkey('enter')

time.sleep(2)

link = "https://www.coursera.org/learn/linux-system-programming-introduction-to-buildroot/home/week/1"
webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open(link)
dirpath = os.path.dirname(os.path.realpath(__file__))
pointxy = None
while pointxy is None:
    pointxy = pyautogui.locateOnScreen(r""+dirpath+"\Advanced_Linux_Command_Line.png",confidence=0.1)

if pointxy is not None:
    pyautogui.moveTo(pointxy[0]+800,pointxy[1]+720,duration=0.8)
    print(pyautogui.position())
    time.sleep(0.5)

time.sleep(6)
pyautogui.click()
time.sleep(4)
```

#### Requirements
- `pyautogui`: Install using `pip install pyautogui`
- `webbrowser` and `os` modules (included with Python standard library)

#### Notes

- Ensure that the Brave browser is installed and accessible on your system.
- Adjust the path to the image and `confidence` parameter as needed to match the image you want to locate on the screen.
- Make sure the image `Advanced_Linux_Command_Line.png` is in the same directory as the script or adjust the path accordingly.

