import keyboard
import subprocess

def on_triggered():
	print("triggered")
	#'explorer' for Windows
	#'nautilus' for linux
	subprocess.run(['explorer',r'C:\Users\Pc\Documents\Embedded_Linux_Diploma\1-Python\2-Containers'])

def listen_for_shortcut():
    # Set the desired shortcut key combination (Example: Ctrl + Alt + S)
    shortcut = "ctrl + alt + s"

    # Register the callback function for the shortcut
    keyboard.add_hotkey(shortcut, on_triggered)

    # Continuously listen for keyboard events
    keyboard.wait()


# Start listening for the shortcut
listen_for_shortcut()
