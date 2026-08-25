from tkinter import *

def c():
    k=float(e.get())
    g = k*1000
    e1.delete(0,END)
    e1.insert(0,g)

    p=float(e.get())
    g = p*2.205
    e2.delete(0,END)
    e2.insert(0,g)

    p=float(e.get())
    g = p*35.274
    e3.delete(0,END)
    e3.insert(0,g)

root = Tk()
root.geometry("500x500")
root.title("weight converter")

l = Label(root, text = "Kg", font = ("Arial", 20))
l.grid(column=0, row=0)

l1 = Label(root, text = "Pounds", font = ("Arial", 20))
l1.grid(row=0, column=1)

e = Entry(root)
e.grid(row=0, column=1)

b = Button(root, text = "convert", font =("Arial", 20), command = c)
b.grid(row=0, column=2)

l2 = Label(root, text = "gram", font = ("Arial", 20))
l2.grid(column=0, row=1)

l3 = Label(root, text = "pound", font = ("Arial", 20))
l3.grid(column=1, row=1)

l4 = Label(root, text = "ounce", font = ("Arial", 20))
l4.grid(column=2, row=1)

e1 = Entry(root, width = 15)
e1.grid(row=2, column=0)

e2 = Entry(root, width = 15)
e2.grid(row=2, column=1)

e3 = Entry(root, width = 15)
e3.grid(row=2, column=2)

       
root.mainloop()