from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.geometry("500x500")
root.title("math")

def f():
    global a1
    r = random.randint(1, 10)
    r1 = random.randint(1, 10)
    messagebox.showinfo("quiz", "Calculate the product of " + str(r) + " and " + str(r1))
    a1=r*r1

def m():
    g=int(e.get())
    if g==a1:
        messagebox.showinfo("results", "correct! you are a math whiz!")
    else:
        messagebox.showinfo("results", "wrong! the answer was " + str(a1))
    e.delete(0,END)

l=Label(root, text="Quiz", font=("Arial", 20))
l.grid(row=0,column=0)

b=Button(root, text="quiz", font=("Arial", 20), command=f)
b.grid(row=1,column=0)

e=Entry(root)
e.grid(row=2,column=0)

b1=Button(root, text="check", font=("Arial", 20), command=m)
b1.grid(row=3,column=0)

root.mainloop()