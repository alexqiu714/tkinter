from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.geometry("500x500")
root.title("ls")

l=Label(root,text="0")
l.grid(row=0, column=0)

l1=Label(root,text="0")
l1.grid(row=0, column=1)

l2=Label(root,text="0")
l2.grid(row=0, column=2)

def c():
    r=random.randint(0,9)
    r1=random.randint(0,9)
    r2=random.randint(0,9)
    l.config(text= str(r))
    l1.config(text= str(r1))
    l2.config(text= str(r2))
    if r == r1 and r == r2:
        messagebox.showinfo("Win", "JACKPOT! You win 1000$")
    if r == r1 or r==r2 or r1==r2:
        messagebox.showinfo("Win", "Mini prize! You win 10$")

b=Button(root,text="Spin", command=c)
b.grid(row=1, column=0, columnspan=3)

root.mainloop()