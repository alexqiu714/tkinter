from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.geometry("500x500")
root.title("gtn")

def c():
    v=e.get()
    b.config(state="disabled")
    b1.config(state="normal")
    messagebox.showinfo("tutorial", "hi " + v + ",im thinking of a number between 1-20, can you guess it?")

r1 = random.randint(1, 20)

def r():
    g = int(e1.get())
    if g>r1:
        messagebox.showinfo("hint", "your number is too high!")
    elif g<r1:
        messagebox.showinfo("hint", "your number is too low!")
    else:
        messagebox.showinfo("hint", "correct!")

l=Label(root, text="Guess the number", font=("Arial", 35))
l.grid(row=0,column=0)

l=Label(root, text="enter your name", font=("Arial", 15))
l.grid(row=1,column=0)

e = Entry(root)
e.grid(row=2,column=0)

b=Button(root,text="next", font=("Arial", 20), command=c)
b.grid(row=2,column=1)

l=Label(root, text="guess the number", font=("Arial", 15))
l.grid(row=3,column=0)

e1 = Entry(root)
e1.grid(row=4,column=0)

b1=Button(root,text="guess", font=("Arial", 20), state="disabled", command=r)
b1.grid(row=4,column=1)

root.mainloop()