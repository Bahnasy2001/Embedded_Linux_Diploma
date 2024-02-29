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
