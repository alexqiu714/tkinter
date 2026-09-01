from tkinter import *
from time import strftime

root=Tk()
root.geometry("500x500")
root.title("digital clock")

mode = "24"

def t(): 
    if mode=="24":
        l1.config(text=strftime("%H: %M: %S"))
        l1.after(1000,t)
    elif mode=="12":
        l1.config(text=strftime("%I: %M: %S %p"))
        l1.after(1000,t)

def t24():
    global mode
    mode="24"

def t12():
    global mode
    mode="12"

l = Label(root, text = strftime("%d/%m/%Y"), font = ("Arial", 20))
l.grid(row=0, column=0)

l1 = Label(root, text = strftime("%H: %M: %S"), font = ("Arial", 20))
l1.grid(row=1, column=0)

b = Button(root, text = "change to 12 hour clock", font = ("Arial", 20), command = t12)
b.grid(row=2, column=0)

b = Button(root, text = "change to 24 hour clock", font = ("Arial", 20), command = t24)
b.grid(row=2, column=1)

t()

root.mainloop()