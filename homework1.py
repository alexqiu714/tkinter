from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("discount")

def answer():
    a = float(e.get())
    a1 = float(e1.get())
    r = a * (1 - a1/100)
    r1 = a * (a1/100)
    e3.insert(0,r)
    e2.insert(0,r1)

l = Label(root, text = "original price", font = ("Arial", 20))
l.grid(row=0, column=0)

e = Entry(root)
e.grid(row=0, column=1)

l1 = Label(root, text = "discount (%)", font = ("Arial", 20))
l1.grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=1, column=1)

b= Button(root, text = "calculate", font = ("Arial", 20), command = answer)
b.grid(row=2, column=0)

l2 = Label(root, text = "amount saved", font = ("Arial", 20))
l2.grid(row=3, column=0)

e2 = Entry(root)
e2.grid(row=3, column=1)

l3 = Label(root, text = "final price", font = ("Arial", 20))
l3.grid(row=4, column=0)

e3 = Entry(root)
e3.grid(row=4, column=1)

root.mainloop()