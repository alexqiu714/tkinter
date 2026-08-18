from tkinter import *

def result():
    answer = int(e.get())*int(e2.get())
    r = Label(root, text=answer)
    r.grid(row=3, column=1)


root=Tk()
root.geometry("500x400")
root.title("Mini Adder")

ml = Label(root, text="Length:", font=("Arial", 20))
ml.grid(row=0, column=0)

ml = Label(root, text="Width:", font=("Arial", 20))
ml.grid(row=0, column=2)

e = Entry(root)
e.grid(row=1, column=0)

e2 = Entry(root)
e2.grid(row=1, column=2)

b = Button(root, text="Calculate Area", font=("Arial", 20), command = result)
b.grid(row=2, column=0)

rl = Label(root, text="Area: ", font=("Arial", 20))
rl.grid(row=3, column=0)

root.mainloop()