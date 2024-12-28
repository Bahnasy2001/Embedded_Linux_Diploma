from tkinter import *


def validate():
    try:
        m = int(e1.get())
        n = int(e2.get())
        if v.get() == 1:  # Subtraction
            result = m - n
            result_message = f"The Difference is: {m} - {n} = {result}"
        elif v.get() == 2:  # Addition
            result = m + n
            result_message = f"The Sum is: {m} + {n} = {result}"
        else:
            result_message = "Select an operation"
        result_label.config(text=result_message)
    except ValueError:
        result_label.config(text="Invalid input")
master = Tk()
v = IntVar()
master.title("Quick_Task3")
label1 = Label(master,text="Enter The Value of M: ")
label2 = Label(master,text="Enter The Value of N: ")
btn = Button(master,text="Validate", command=validate)
sub = Radiobutton(master,text="sub",fg="red",variable=v,value=1)
sum = Radiobutton(master,text="sum",fg="blue",variable=v,value=2)
e1 = Entry(master)
e2 = Entry(master)
result_label = Label(master)
#arrangemnet

label1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
e1.grid(row=0, column=1, padx=10, pady=5)

label2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
e2.grid(row=1, column=1, padx=10, pady=5)
result_label.grid(row=3, column=0, columnspan=2, pady=10)
btn.grid(row=4, column=0, columnspan=2)

sub.grid(row=5, column=0, padx=10,sticky=W)
sum.grid(row=6, column=0, padx=10,sticky=W)
master.mainloop()