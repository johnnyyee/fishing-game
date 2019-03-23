from tkinter import *
import fishing

# ** Recipe ***
# 1 Window
# 2 Buttons
# 5 Labels

def fishh():
    fishing.fish()
    caught.config(text=fishing.turn.result)


w = Tk()
w.title("test")

fishbutton = Button(w, text="Fish!",command=fishh)
fishbutton.pack()
stopbutton = Button(w, text="Stop!")
stopbutton.pack()

p1n = Label(w, text="Player 1")
p1n.pack()
p2n = Label(w, text="Player 2")
p2n.pack()

p1p = Label(w, text="Player 1 Points:")
p1p.pack()
p2p = Label(w, text="Player 2 Points")
p2p.pack()

caught = Label(w, text="test")
caught.pack()