import tkinter as tk
master = tk.Tk()
master.geometry("300x200")
def reverse():
    # Retrieve the text from the entry widget
    text = e1.get()
    reversed_text = text[::-1]
    tk.Label(master,text=reversed_text).place(x=100,y=70)
    print(reversed_text)
    return reversed_text

master.title("Quick_Task2")
tk.Label(master,text="Enter a word: ").place(x=20,y=40)
e1 = tk.Entry(master)
e1.place(x=100,y= 40)
btn = tk.Button(master,text="Validate",width=17,command=reverse).place(x=100,y=100)
master.mainloop()
