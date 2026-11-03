from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.geometry("500x500")
root.title("ttt")

board=[]

def onclick(row,column):
    global cp
    global count
    global mode
    if board[row][column]["text"]=="":
        board[row][column]["text"]=cp
        if mode=="single" and cp=="o":
            c()
        else:
            if cp=="x":
                cp="o"
            elif cp=="o":
                cp="x"
        count += 1
    if count==9:
        messagebox.showinfo("result", "Draw!")
        r()
        gameover=True

    winner=w()

    if winner:
        messagebox.showinfo("result", winner + " won!")
        gameover=True
        r()

def r():
    global cp
    global gameover
    for row in range(3):
        for column in range(3):
            board[row][column]["text"]=""
    gameover=False  
    cp="x"

def w():
    for r in range(3):
        if board[r][0]["text"]==board[r][1]["text"]==board[r][2]["text"]!=" ":
            return board[r][0]["text"]  
    for c in range(3):
        if board[0][c]["text"]==board[1][c]["text"]==board[2][c]["text"]!=" ":
            return board[0][c]["text"]  
    if board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]!=" ":
        return board[0][0]["text"]
    if board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]!=" ":
        return board[0][2]["text"]    
    return None

cp="x"

gameover=False

count=0

mode="multi"

def m(x):
    global mode
    mode=x
    r()

def c():
    global gameover
    global count
    global cp
    el=[]
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"]=="":
                el.append((row,column))
    if el:
        r,c=random.choice(el)
        board[r][c]["text"]=="o"
        count+=1
        winner=w()
        if winner:
            messagebox.showinfo("result", winner + " won!")
            gameover=True
            r()
        else:
            cp="x"

for row in range(3):
    newrow=[]
    for column in range(3):
        newrow.append(None)
    board.append(newrow)

b=Button(root,text="Singleplayer", command=lambda:m("Single"))
b.grid(row=3, column=0)

b1=Button(root,text="Multiplayer", command=lambda:m("Multi"))
b1.grid(row=3, column=2)

for row in range(3):
    for column in range(3):
        board [row][column] = Button(root, width=15, height=8, command=lambda r=row, c=column:onclick(r,c))
        board [row][column].grid(row=row, column=column)

root.mainloop()
