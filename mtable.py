from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
root.geometry("400x600")
root.title("mtable")

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

r=Radiobutton(root, text="20", variable=i, value=10)
r.grid(row=3,column=1)

r=Radiobutton(root, text="30", variable=i, value=10)
r.grid(row=4,column=1)

b=Button(root, text="Generate", font=("Arial", 20))
b.grid(row=3,column=0)

l1=Label(root)
l1.grid(row=4,column=0)

root.mainloop()