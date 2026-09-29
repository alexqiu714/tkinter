from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("memoriser")

def a():
    g=e.get()
    l.insert(0,g)
    e.delete(0,END)

def c():
    l.delete(0,END)

b=Button(root, text="Save")
b.grid(row=0,column=1)

e=Entry(root)
e.grid(row=1,column=1)

b1=Button(root, text="Add", command=a)
b1.grid(row=2,column=1)

b2=Button(root, text="Open")
b2.grid(row=3,column=0)

b3=Button(root, text="Clear", command=c)
b3.grid(row=3,column=1)

b4=Button(root, text="Delete")
b4.grid(row=3,column=2)

l=Listbox(root, width=30,height=23)
l.grid(row=4,column=1)

for i in range(1,101):
    l.insert(END,"List "+ str(i))

root.mainloop()