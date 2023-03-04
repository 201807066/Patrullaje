import tkinter
from tkinter import *
top = tkinter.Tk()
top.title("Welcome to innovate app")
top.geometry("350x200")
labl = Label(top, text="Usuario")
labl.grid(column=0, row=0)
txtUser = Entry(top, width=10)
txtUser.grid(column=1, row=0)

labl1 = Label(top, text="Pass")
labl1.grid(column=0, row=3)
txtPass = Entry(top, width=10)
txtPass.grid(column=1, row=3)

def click():
    if txtUser.get() == "user" and txtPass.get() == "pass":
        labl.configure(text="SI")
    else:
        labl.configure(text="NO")

	

btn = Button(top, text ="Ingresar", command=click)
btn.grid(column=2, row=0)
top.mainloop()