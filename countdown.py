from tkinter import *
from tkinter import messagebox

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
    c()

def c():
    global total
    min,sec=divmod(total,60)
    hour,min=divmod(min,60)
    h.set(hour)
    m.set(min)
    s.set(sec)
    if total == 0:
        messagebox.showinfo("time", "Times up!")
        e.config(state="normal")
        e1.config(state="normal")
        e2.config(state="normal")
        b.config(state="normal")
        return
    total -= 1
    root.after(1000, c)

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