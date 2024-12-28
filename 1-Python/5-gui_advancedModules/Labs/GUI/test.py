##################### Lab 1 #########################
# import tkinter
# m=tkinter.Tk()#where m is the name of the main window object
# m.mainloop()
#####################################################
##################### Lab 2 #########################
# from tkinter import *
# window=Tk()
# window.title("Hassan")
# window.geometry("500x500+150+200")
# window.mainloop()
#####################################################
##################### Lab 3 #########################
# from tkinter import *
# window=Tk()
# window.title("Hassan")
# window.geometry("500x500+150+200")
# window.resizable(False,False)
# window.mainloop()
#####################################################
##################### Lab 4 #########################
# from tkinter import *
# window=Tk()
# window.title("Hassan")
# window.geometry("500x500+150+200")
# window.resizable(False,False)
# window.configure(background="black")
# window.mainloop()
#####################################################
##################### Lab 5 #########################
# from tkinter import *
# window=Tk()
# window.title("Hassan")
# window.geometry("500x500+150+200")
# window.resizable(False,False)
# window.configure(background="Green")
# Label(window,text="Bahnasy",fg="red",bg="black").pack()
# window.mainloop()
#####################################################
##################### Lab 6 #########################
# from tkinter import *
# window=Tk()
# window.title("Hassan")
# window.geometry("500x500+150+200")
# window.resizable(False,False)
# window.configure(background="Green")
# Label(window,text="Bahnasy",fg="red",bg="black").grid(row=0,column=0)
# Label(window,text="hello",fg="red",bg="black").grid(row=0,column=1)
# window.mainloop()
#####################################################
##################### Lab 7 #########################
# from tkinter import *
# window=Tk()
# window.title("Hassan")
# window.geometry("500x500+150+200")
# window.resizable(False,False)
# window.configure(background="Green")
# Label(window,text="Bahnasy",fg="red",bg="black").place(x=20,y=20)
# Label(window,text="hello",fg="red",bg="black").place(x=75,y=20)
# window.mainloop()
#####################################################
##################### Lab 8 #########################
# import tkinter as tk
# m = tk.Tk()
# m.title("Counting Seconds")
# m.geometry("500x500+150+200")
# button = tk.Button(m,text='Stop',width=25,command=m.destroy)
# button.pack()
# m.mainloop()
#####################################################
##################### Lab 9 #########################
# import tkinter as tk
# def Led_on():
#     print("Led is on")
# m = tk.Tk()
# m.title("Counting Seconds")
# m.geometry("500x500+150+200")
# button = tk.Button(m,text='Led on',fg="#FFFFFF",bg="black",width=25,command=Led_on)
# button.pack()
# m.mainloop()
#####################################################
##################### Lab 10 ########################
# from tkinter import *
# root = Tk()
# frame = Frame(root)
# frame.pack()
# bottomframe = Frame(root)
# bottomframe.pack(side = BOTTOM)
# redbutton = Button(frame,text="Red",fg='red')
# redbutton.pack(side= LEFT)
# brownbutton = Button(frame,text="Brown",fg='brown')
# brownbutton.pack(side= LEFT)
# bluebutton = Button(frame,text="Blue",fg='blue')
# bluebutton.pack(side= LEFT)
# blackbutton = Button(bottomframe,text="Black",fg="black")
# blackbutton.pack(side=BOTTOM)
# root.mainloop()
#####################################################
##################### Lab 11 ########################
# import tkinter as tk
# master = tk.Tk()
# tk.Label(master,text="First Name").grid(row=0)
# tk.Label(master,text="Last Name").grid(row=1)
# e1 = tk.Entry(master)
# e2 = tk.Entry(master)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# tk.mainloop()
#####################################################
##################### Lab 12 ########################
# from tkinter import *

# def items_selected(event):
#     # get Selected indices
#     selected_index = Lb.curselection()
#     # get Selected item
#     print(selected_index)
#     print(Lb.get(selected_index))
    
# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1,"python")
# Lb.insert(2,"Java")
# Lb.insert(3,"C++")
# Lb.insert(4,"Any Other")
# Lb.pack()
# Lb.bind('<<ListboxSelect>>', items_selected)
# top.mainloop()
#####################################################
##################### Lab 13 ########################
# from tkinter import *
# root = Tk()
# v = IntVar()
# Radiobutton(root,text="DevOps",variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text="Embedded Linux",variable=v,value=2).pack(anchor=W)
# mainloop()
#####################################################
##################### Lab 14 ########################
# from tkinter import *

# def DisplayValue():
#     global v
#     print(v.get())
# root = Tk()
# v = IntVar()
# Radiobutton(root,text="DevOps",variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text="Embedded Linux",variable=v,value=2).pack(anchor=W)
# button = Button(root,text="GET",width=25,command=DisplayValue)
# button.pack()
# mainloop()
#####################################################
##################### Lab 15 ########################
# import tkinter
# parent_widget = tkinter.Tk()
# checkbutton_widget = tkinter.Checkbutton(parent_widget,text="Checkbutton")
# checkbutton_widget.select()
# checkbutton_widget.pack()
# tkinter.mainloop()
#####################################################
##################### Lab 16 ########################
# import tkinter
# parent_widget = tkinter.Tk()
# scale_widget = tkinter.Scale(parent_widget,from_=0,to=100,orient=tkinter.HORIZONTAL)
# scale_widget.set(25)
# scale_widget.pack()
# tkinter.mainloop()
#####################################################
##################### Lab 17 ########################
# import tkinter
# parent_widget = tkinter.Tk()
# text_widget = tkinter.Text(parent_widget,width=20,height=3)

# text_widget.insert(tkinter.END,"Text Widgetn20 characters widen3 lines high")
# text_widget.insert(tkinter.END," Hassan")
# text_widget.pack()
# tkinter.mainloop()
#####################################################
##################### Lab 18 ########################
# from tkinter import *
# master = Tk()
# def openNewWindow():
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(master)
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("New Window") 
#     # sets the geometry of toplevel
#     newWindow.geometry ("200x200")
#     # A Label widget to show in toplevel
#     Label (newWindow,text="This is a new window").pack()
    
# label = Label(master,text="This is the main window")
# label.pack(pady=10)
# btn = Button(master,text="Click to open a new window",command=openNewWindow)
# btn.pack(pady=10)
# mainloop()
#####################################################
from tkinter import *
 
 
root = Tk()
 
C = Canvas(root, bg="yellow",
           height=250, width=300)
 
line = C.create_line(108, 120,
                     320, 40,
                     fill="green")
 
arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")
 
oval = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")
 
C.pack()
mainloop()