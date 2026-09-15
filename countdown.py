from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("countdown")

def d():
    global total
    e.config(state="disabled")
    e1.config(state="disabled")
    e2.config(state="disabled")
    b.config(state="disabled")
    total=(int(h.get())*3600)+(int(m.get())*60)+(int(s.get()))

def c():
    min,sec=divmod(total,60)
    hour,min=divmod(min,60)

h=StringVar()
h.set("00")

m=StringVar()
m.set("00")

s=StringVar()
s.set("00")

e=Entry(root, width=5, textvariable=h)
e.grid(row=0,column=0)

e1=Entry(root, width=5, textvariable=m)
e1.grid(row=0,column=1)

e2=Entry(root, width=5, textvariable=s)
e2.grid(row=0,column=2)

b=Button(root,text="start countdown", font=("Arial", 20), command=d)
b.grid(row=1,column=0,columnspan=3)

root.mainloop()