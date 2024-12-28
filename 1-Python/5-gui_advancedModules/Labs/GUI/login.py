from tkinter import *
def Login():
    print("Welcome ",e1.get())
    print("Second name is ",e2.get())
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
btn = Button(master,text="Login",command=Login).grid(row=2,column=0)
master.mainloop()