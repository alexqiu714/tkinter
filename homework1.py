from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.geometry("500x500")
root.title("color change")

l=Listbox(root, width=30,height=23)
l.grid(row=5,column=0)
l1=["blue","red","yellow"]
for i in l1:
    l.insert(END, i)

def a():
    g=e.get()
    l.insert(END, g)

def c():
    l.delete(0, END)

def d():
    index=l.curselection()
    l.delete(index)

def a1():
    bc=l.curselection()
    z=l.get(bc)
    root.config(bg=z)

e=Entry(root)
e.grid(row=0,column=0)

b=Button(root, text="Add", command=a)
b.grid(row=1,column=0)

b1=Button(root, text="Delete", command=d)
b1.grid(row=2,column=0)

b2=Button(root, text="Apply", command=a1)
b2.grid(row=3,column=0)

b3=Button(root, text="Clear", command=c)
b3.grid(row=4,column=0)

root.mainloop()