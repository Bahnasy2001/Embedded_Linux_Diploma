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
