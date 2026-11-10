from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("adress book")

l=Label(root,text="My adress book")
l.grid(row=0,column=0)

b=Button(root,text="Open")
b.grid(row=0,column=1)

l1=Label(root,text="Name")
l1.grid(row=1,column=0)

l2=Label(root,text="Address")
l2.grid(row=2,column=0)

l3=Label(root,text="Mobile")
l3.grid(row=3,column=0)

l4=Label(root,text="Email")
l4.grid(row=4,column=0)

l5=Label(root,text="Birthday")
l5.grid(row=5,column=0)

e=Entry(root)
e.grid(row=1,column=2)

e1=Entry(root)
e1.grid(row=2,column=2)

e2=Entry(root)
e2.grid(row=3,column=2)

e3=Entry(root)
e3.grid(row=4,column=2)

e4=Entry(root)
e4.grid(row=5,column=2)

e5=Entry(root)
e5.grid(row=6,column=2)

b1=Button(root,text="Update/add")
b1.grid(row=7,column=2)

b2=Button(root,text="Edit")
b2.grid(row=7,column=0)

b3=Button(root,text="Delete")
b3.grid(row=7,column=1)

root.mainloop()