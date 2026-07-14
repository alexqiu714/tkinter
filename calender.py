from tkinter import *

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

b = Button(root, text="Show calender", font=("Arial", 20))
b.grid(row=2,column=0, columnspan=20)



root.mainloop()