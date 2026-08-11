from tkinter import *
import calendar

def cal():
    root2 = Tk()
    root2. geometry("800x800")
    root2.title("caldisplay")
    c =int (e.get())
    getcal = calendar.calendar(c)
    sc = Label(root2, text=getcal)
    sc.grid(row=0, column=0)
    root2.mainloop()

root = Tk()
root.geometry("500x500")
root.config(background="red")
root.title("calender")

cl = Label(root, text="Calender", font=("Arial", 40, "bold"), bg="blue")
cl.grid(row=0,column=0, columnspan=20)

sl = Label(root, text="Enter year:", font=("Arial", 25))
sl.grid(row=1,column=0)
e = Entry(root)
e.grid(row=1,column=2)

b = Button(root, text="Show calender", font=("Arial", 20), command = cal)
b.grid(row=2,column=0, columnspan=20)



root.mainloop()