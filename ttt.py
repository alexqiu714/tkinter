from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("ttt")

board=[]

def onclick(row,column):
    board[row][column]["text"]=cp

def w():
    for r in range(3):
        if board[r][0]["text"]==board[r][1]["text"]==board[r][2]["text"]!=" "
            return board[r][0]["text"]  
    for c in range(3):
        if board[0][c]["text"]==board[1][c]["text"]==board[2][c]["text"]!=" "
            return board[0][c]["text"]  
        if board[0][c]["text"]==board[1][c]["text"]==board[2][c]["text"]!=" "
            return board[0][c]["text"]  

cp="x"

gamemode="single"
gameover=false

count=0

for row in range(3):
    newrow=[]
    for column in range(3):
        newrow.append(None)
    board.append(newrow)

for row in range(3):
    for column in range(3):
        board [row][column] = Button(root, width=15, height=10, command=lambda r=row, c=column:onclick(r,c))
        board [row][column].grid(row=row, column=column)


root.mainloop()
