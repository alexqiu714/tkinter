from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
root.geometry("400x600")
root.title("mtable")

def p():
    n1 = n.get()
    n2 = i.get()
    t = ""
    for i1 in range(1,n2+1):
        t+=str(n1)+ " * " + str(i1)+ " = " + str(n1*i1) +"\n"
    l1.config(text=t)

l=Label(root, text="Mathematical table", font=("Arial", 25))
l.grid(row=0,column=0)

l1=Label(root, text="number and range:", font=("Arial", 20))
l1.grid(row=1,column=0)

n = IntVar()
c=Combobox(root, textvariable=n)
c["values"] = list(range(1,101))
c.grid(row=2,column=0)

i=IntVar()
r=Radiobutton(root, text="10", variable=i, value=10)
r.grid(row=2,column=1)

r1=Radiobutton(root, text="20", variable=i, value=20)
r1.grid(row=3,column=1)

r2=Radiobutton(root, text="30", variable=i, value=30)
r2.grid(row=4,column=1)

b=Button(root, text="Generate", font=("Arial", 20), command=p)
b.grid(row=3,column=0)

l1=Label(root)
l1.grid(row=5,column=0)

root.mainloop()