"""
    This is the second version of my tic-tac-toe game.
    As this is my first approach to code in Python with GUI, I'll use the tkinter library. Hopefully for the next version of this game I may use pygame.
"""


from itertools import count
from tabnanny import check
from tkinter import *
import tkinter.messagebox
from turtle import clear
from webbrowser import get

# Board Code

game = Tk()

game.iconbitmap('tic-tac-toe.ico')
game.title('Tic-Tac-Toe-Game')
game.resizable(False, False)

click = True
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xEmoticon = PhotoImage(file='./img/xEmoticonRes.png')
oEmoticon = PhotoImage(file='./img/oEmoticonRes.png')

# Function to define the grid buttons

def startGame():
    button1 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn1, command=lambda: hitBtn(1,0,0))
    button1.grid(row=0, column=0)

    button2 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn2, command=lambda: hitBtn(2,0,1))
    button2.grid(row=0, column=1)

    button3 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn3, command=lambda: hitBtn(3,0,2))
    button3.grid(row=0, column=2)

    button4 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn4, command=lambda: hitBtn(4,1,0))
    button4.grid(row=1, column=0)

    button5 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn5, command=lambda: hitBtn(5,1,1))
    button5.grid(row=1, column=1)

    button6 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn6, command=lambda: hitBtn(6,1,2))
    button6.grid(row=1, column=2)

    button7 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn7, command=lambda: hitBtn(7,2,0))
    button7.grid(row=2, column=0)

    button8 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn8, command=lambda: hitBtn(8,2,1))
    button8.grid(row=2, column=1)

    button9 = Button(game, height=9, width=19, bd=.5, relief='sunken', bg='#3B3430', textvariable=btn9, command=lambda: hitBtn(9,2,2))
    button9.grid(row=2, column=2)

# Tic Tac Toe algorithm

def hitBtn(num, r, c):
    global click, count
    if click == True:
        labelPhoto = Label(game, image=xEmoticon)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('X')
        elif num == 2:
            btn2.set('X')
        elif num == 3:
            btn3.set('X')
        elif num == 4:
            btn4.set('X')
        elif num == 5:
            btn5.set('X')
        elif num == 6:
            btn6.set('X')
        elif num == 7:
            btn7.set('X')
        elif num == 8:
            btn8.set('X')
        else:
            btn9.set('X')
        count += 1
        click = False
        checkWin()

    else:
        labelPhoto = Label(game, image=oEmoticon)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('O')
        elif num == 2:
            btn2.set('O')
        elif num == 3:
            btn3.set('O')
        elif num == 4:
            btn4.set('O')
        elif num == 5:
            btn5.set('O')
        elif num == 6:
            btn6.set('O')
        elif num == 7:
            btn7.set('O')
        elif num == 8:
            btn8.set('O')
        else:
            btn9.set('O')
        count += 1
        click = True
        checkWin()

# Function to check who wins

def checkWin():
    global count, click

    if (btn1.get()=='X' and btn2.get()=='X' and btn3.get()=='X' or
        btn4.get()=='X' and btn5.get()=='X' and btn6.get()=='X' or
        btn7.get()=='X' and btn8.get()=='X' and btn9.get()=='X' or
        btn1.get()=='X' and btn4.get()=='X' and btn7.get()=='X' or
        btn2.get()=='X' and btn5.get()=='X' and btn8.get()=='X' or
        btn3.get()=='X' and btn6.get()=='X' and btn9.get()=='X' or
        btn1.get()=='X' and btn5.get()=='X' and btn9.get()=='X' or
        btn3.get()=='X' and btn5.get()=='X' and btn7.get()=='X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'X Wins!')
        click = True
        count = 0
        clear()
        startGame()

    elif (btn1.get()=='O' and btn2.get()=='O' and btn3.get()=='O' or
        btn4.get()=='O' and btn5.get()=='O' and btn6.get()=='O' or
        btn7.get()=='O' and btn8.get()=='O' and btn9.get()=='O' or
        btn1.get()=='O' and btn4.get()=='O' and btn7.get()=='O' or
        btn2.get()=='O' and btn5.get()=='O' and btn8.get()=='O' or
        btn3.get()=='O' and btn6.get()=='O' and btn9.get()=='O' or
        btn1.get()=='O' and btn5.get()=='O' and btn9.get()=='O' or
        btn3.get()=='O' and btn5.get()=='O' and btn7.get()=='O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'O Wins!')
        count = 0
        clear()
        startGame()

    elif (count == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Tie Game!')
        click = True
        count = 0
        clear()
        startGame()

# Function to clear the game


def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')



startGame()

game.mainloop()