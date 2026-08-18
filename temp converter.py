from tkinter import *

def answer():
    try:
        c=float(e.get())
        a = c*1.8+32
        l2.config(text =str(a) + "F")
    except ValueError:
        l2.config(text = "error: not a number")

root=Tk()
root.geometry("500x500")
root.title("temp converter")

l = Label(root, text = "Celsius", font = ("Arial", 20))
l.grid(column=0, row=0)

l1 = Label(root, text = "Fahrenheit", font = ("Arial", 20))
l1.grid(column=2, row=0)

l2 = Label(root, font = ("Arial", 20))
l2.grid(column=2, row=2)

e = Entry(root)
e.grid(column=0, row=1)

b = Button(root, text = "convert", font = ("Arial", 20), command = answer)
b.grid(column=1, row=2)


root.mainloop()