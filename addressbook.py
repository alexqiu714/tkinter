from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
root.title("adress book")

d={}

def u():
    key=e.get()
    d[key]=(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    li.insert(0, key)
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def ed():
    print("called") 
    index=li.curselection()
    e.insert(0,li.get(index))
    details=d[e.get()]
    e1.insert(0, details[0])
    e2.insert(0, details[1])
    e3.insert(0, details[2])
    e4.insert(0, details[3])
    e5.insert(0, details[4])

def dd(event):
    index1=li.curselection()
    name=li.get(index1)
    d1=d[name]
    ad="name: "+name+"\n"+"address: "+d1[0]+"\n"+"mobile: "+d1[1]+"\n"+"email: "+d1[2]+"\n"+"birthday: "+d1[3]
    messagebox.showinfo("Details", ad)

l=Label(root,text="My address book")
l.grid(row=0,column=0)

b=Button(root,text="Open")
b.grid(row=0,column=1)

l1=Label(root,text="Name")
l1.grid(row=1,column=1)

l2=Label(root,text="Address")
l2.grid(row=2,column=1)

l3=Label(root,text="Mobile")
l3.grid(row=3,column=1)

l4=Label(root,text="Email")
l4.grid(row=4,column=1)

l5=Label(root,text="Birthday")
l5.grid(row=5,column=1)

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

b1=Button(root,text="Update/add", command=u)
b1.grid(row=7,column=2)

b2=Button(root,text="Edit", command=ed)
b2.grid(row=7,column=0)

b3=Button(root,text="Delete")
b3.grid(row=7,column=1)

b4=Button(root,text="Save", width=15)
b4.grid(row=8,column=1)

li=Listbox(root, width=40, height=25)
li.grid(row=1,column=0,rowspan=5)
li.bind('<<ListboxSelect>>',dd)

root.mainloop()