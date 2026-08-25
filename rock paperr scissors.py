from tkinter import *
import random

o = ["Rock", "Paper", "Scissors"]

playerscore = 0
computerscore = 0

def pc(x):
    global playerscore
    global computerscore
    l.config(text="Your input: " + x)
    cc = random.choice(o)
    l1.config(text="Computer input: " + cc)
    if x == cc:
        s.config(text="Draw!")
    elif x == "Rock":
        if cc == "Paper":
            s.config(text="Computer won")
            computerscore += 1
            l3.config(text="Computer score: " + str (computerscore))
        elif cc == "Scissors":
            s.config(text="Player won")
            playerscore += 1
            l2.config(text="Player score: " + str (playerscore))
    elif x == "Paper":
        if cc == "Scissors":
            s.config(text="Computer won")
            computerscore += 1
            l3.config(text="Computer score: " + str (computerscore))
        elif cc == "Rock":
            s.config(text="Player won")
            playerscore += 1
            l2.config(text="Player score: " + str (playerscore))
    elif x == "Scissors":
        if cc == "Rock":
            s.config(text="Computer won")
            computerscore += 1
            l3.config(text="Computer score: " + str (computerscore))
        elif cc == "Paper":
            s.config(text="Player won")
            playerscore += 1
            l2.config(text="Player score: " + str (playerscore))

root=Tk()
root.geometry("600x500")
root.title("rock paper scissors")

h = Label(root, text = "Rock Paper Scissors Shoot", font = ("Arial", 20))
h.pack()

s = Label(root, text = "Start game", font = ("Arial", 17))
s.pack()

f = Frame(root)
f.pack()

p = Label(f, text = "Player options", font = ("Arial", 17))
p.grid(row=0, column=0)

r = Button(f, text="Rock", font = ("Arial", 15), command = lambda:pc(o[0]))
r.grid(row=0, column=1)

pa = Button(f, text="Paper", font = ("Arial", 15), command = lambda:pc(o[1]))
pa.grid(row=0, column=2)

si = Button(f, text="Scissors", font = ("Arial", 15), command = lambda:pc(o[2]))
si.grid(row=0, column=3)

l = Label(f, text="Your input: ", font = ("Arial", 15))
l.grid(row=1, column=0)

l1 = Label(f, text="Computers input: : ", font = ("Arial", 15))
l1.grid(row=2, column=0)

l2 = Label(f, text="Player score: " + str (playerscore), font = ("Arial", 15))
l2.grid(row=1, column=2)

l3 = Label(f, text="Computer score: " + str (computerscore), font = ("Arial", 15))
l3.grid(row=2, column=2)

root.mainloop()