import keyboard
import subprocess
import datetime

def on_triggered():
    """
    Callback function executed when the specified shortcut key combination is pressed.
    Writes the current date and time to a text file.
    """
    print("triggered")  # Print a message to the console
    
    # Open the file in write mode. Update the path if needed for your system.
    with open(r'C:\Users\Pc\Documents\Embedded_Linux_Diploma\1-Python\2-Containers\date.txt', 'w') as file:
        # Write the current date and time to the file
        file.write(str(datetime.datetime.now()))

def listen_for_shortcut():
    """
    Sets up a hotkey and starts listening for it.
    Registers the callback function to be called when the shortcut is pressed.
    Continuously listens for keyboard events.
    """
    # Set the desired shortcut key combination (Example: Ctrl + Alt + S)
    shortcut = "ctrl + alt + s"

    # Register the callback function for the shortcut
    keyboard.add_hotkey(shortcut, on_triggered)

    # Continuously listen for keyboard events
    keyboard.wait()

# Start listening for the shortcut
listen_for_shortcut()
