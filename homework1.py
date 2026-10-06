from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
root.geometry("500x500")
root.title("pizza app")

l=Label(root, text="Welcome to Pizza Hut", font=("Arial", 25))
l.grid(row=0, column=0)

l1=Label(root, text="Select pizza:")
l1.grid(row=1, column=0)

p=StringVar()
c=Combobox(root, textvariable=p)
c["values"]=["Margherita", "Salami", "Prosciutto", "Vegetable"]
c.grid(row=1,column=1)

q=StringVar()
c1=Combobox(root, textvariable=q)
c1["values"]=["1", "2", "3"]
c1.grid(row=2,column=1)

f = Frame(root)
f.grid(row=3,column=1)

s=StringVar()
r=Radiobutton(f, text="s", variable=s, value="small")
r.grid(row=3, column=1)

r1=Radiobutton(f, text="m", variable=s, value="medium")
r1.grid(row=3, column=2)

r2=Radiobutton(f, text="l", variable=s, value="large")
r2.grid(row=3, column=3)

l2=Label(root, text="Enter quantithy:")
l2.grid(row=2, column=0)

l3=Label(root, text="Enter size:")
l3.grid(row=3, column=0)

def r():
    g=s.get()
    q1=q.get()
    p1=p.get()
    l4.config(text="You ordered " + q1 + " " + p1 +  " " + g + " size pizzas")

b=Button(root, text="Order", command=r)
b.grid(row=4,column=1)

l4=Label(root)
l4.grid(row=5,column=0)

root.mainloop()