from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x500")
root.title("kitchen timer")

def s():
    global t
    e1.config(state="disabled")
    e2.config(state="disabled")
    b.config(state="disabled")
    b1.config(state="disabled")
    b2.config(state="disabled")
    t=3*60
    c()


def c():
    global t
    min,sec=divmod(t,60)
    m.set(min)
    s1.set(sec)
    if t == 0:
        messagebox.showinfo("time", "Times up!")
        e1.config(state="normal")
        e2.config(state="normal")
        b.config(state="normal")
        b1.config(state="normal")
        b2.config(state="normal")
        return
    t -= 1
    root.after(1000, c)



#def i():


m=StringVar()
m.set("00")

s1=StringVar()
s1.set("00")

e1=Entry(root, width=5, textvariable=m)
e1.grid(row=0,column=1)

e2=Entry(root, width=5, textvariable=s1)
e2.grid(row=0,column=2)

b=Button(root,text="3 min", font=("Arial", 20), command=s)
b.grid(row=1,column=0)

b1=Button(root,text="5 min", font=("Arial", 20))
b1.grid(row=1,column=1)

b2=Button(root,text="10 min", font=("Arial", 20))
b2.grid(row=1,column=2,columnspan=3)

root.mainloop()