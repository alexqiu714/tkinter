from tkinter import *

root = Tk()
root.geometry("500x500")
root.config(background="light grey")
root.title("Login")

cl = Label(root, text="login", font=("Arial", 30, "bold"), bg="black")
cl.grid(row=0,column=0, columnspan=2, padx = 50)

sl = Label(root, text="Username:", font=("Arial", 20))
sl.grid(row=1,column=0, pady = 13, padx = 50)

p = Label(root, text="Password:", font=("Arial", 20))
p.grid(row=2,column=0, pady = 13, padx = 50)


e = Entry(root)
e.grid(row=1,column=1, pady = 13, padx = 10)

e2 = Entry(root)
e2.grid(row=2,column=1, pady = 13, padx = 10)



root.mainloop()