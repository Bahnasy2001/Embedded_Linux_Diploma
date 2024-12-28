import tkinter as tk

master = tk.Tk()
master.geometry("400x400")

canvas = tk.Canvas(master, width=400, height=400, bg="gray", highlightthickness=0)
canvas.grid(row=0, column=0, padx=0, pady=0)

# Create label and oval as global variables
status_label = tk.Label(master, text="")
status_label.place(x=150, y=300)
oval = canvas.create_oval(50, 50, 140, 150, fill="white")

def LED_ON():
    status_label.config(text="Led is ON")  # Update existing label
    canvas.itemconfig(oval, fill="red")    # Update existing oval
    
def LED_OFF():
    status_label.config(text="Led is OFF") # Update existing label
    canvas.itemconfig(oval, fill="white")  # Update existing oval

btn_One = tk.Button(master, text="Led ON", width=17, command=LED_ON)
btn_Two = tk.Button(master, text="Led OFF", width=17, command=LED_OFF)
btn_One.place(x=150, y=350)
btn_Two.place(x=150, y=380)

master.mainloop()