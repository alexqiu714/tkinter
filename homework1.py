from tkinter import *
from time import strftime
import random

c = ["red","blue","green","purple"]

def t():
    l.config(text=strftime("%X"))
    l.after(1000, t)
    r = random.choice(c)
    root.config(bg=r)    

root=Tk()
root.geometry("500x500")
root.title("Party Clock")

l = Label(root, text=strftime("%X"), font=("Arial", 50))
l.grid(row=0, padx=150,column=0, pady=175)

t()

root.mainloop()