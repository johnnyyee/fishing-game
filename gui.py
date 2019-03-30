from tkinter import *
import fishing

# ** Recipe ***
# 1 Window
# 2 Buttons
# 5 Labels

def fishh():
    fishing.fish()
    caught.config(text=fishing.Turn.result)
    if fishing.Turn.switch:
        endturn()
    if fishing.Turn.player1turn: 
        p1p.config(text=("Player 1 Points:",fishing.Points.p1))
    else:
        p2p.config(text=("Player 2 Points:",fishing.Points.p2))
    
def endturn():
    if fishing.Turn.player1turn:
        fishing.Turn.player1turn = False
        p1n.config(fg="black")
        p2n.config(fg="green")
    else:
        fishing.Turn.player1turn = True
        p2n.config(fg="black")
        p1n.config(fg="green")
    fishing.Turn.switch = False


w = Tk()
w.title("test")

fishbutton = Button(w, text="Fish!",command=fishh)
fishbutton.pack()
stopbutton = Button(w, text="Stop!",command=endturn)
stopbutton.pack()


p1n = Label(w, text="Player 1",fg="green")
p1n.pack()
p2n = Label(w, text="Player 2")
p2n.pack()

p1p = Label(w, text="Player 1 Points:")
p1p.pack()
p2p = Label(w, text="Player 2 Points")
p2p.pack()

caught = Label(w, text="test")
caught.pack()