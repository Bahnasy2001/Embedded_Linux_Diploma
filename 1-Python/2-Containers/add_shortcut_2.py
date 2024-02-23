import keyboard
import subprocess
import datetime

def on_triggered():
	print("teiggered")
	file = open(r'C:\Users\Pc\Documents\Embedded_Linux_Diploma\1-Python\2-Containers\date.txt','w')
	file.write(str(datetime.datetime.now()))
	file.close()


def listen_for_shortcut():
	shortcut = "ctrl + alt + s"
	keyboard.add_hotkey(shortcut,on_triggered)
	keyboard.wait()


listen_for_shortcut()