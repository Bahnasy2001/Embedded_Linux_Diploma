import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Quick_Task")
Button_one = tk.Button(window,text="Button1").grid(row=0,column=1)
Button_two = tk.Button(window,text="Button2").grid(row=1,column=0)
Button_three = tk.Button(window,text="Button3").grid(row=1,column=2)
Button_four = tk.Button(window,text="Button4").grid(row=2,column=1)
window.mainloop()