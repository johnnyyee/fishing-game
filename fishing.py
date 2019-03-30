import random


uc = "You caught"

fish1 = "a.. sock? +0"
fish2 = "a plankter... +1"
fish3 = "a catfish. +3"
fish4 = "a giant squid! +5"
fish5 = "a MEGALODON!!! +10"



class Turn:
    player1turn = True
    result = ""
    switch = False
    
class Points:
    p1 = 0
    p2 = 0

def fish():    
    num = random.randint(1,6)
    
    if num == 1:
        Turn.result = (uc, fish1)
    
    elif num == 2:
        Turn.result = (uc, fish2)
        if Turn.player1turn:
            Points.p1 += 1
        else:
            Points.p2 += 1
        
    elif num == 3:
        Turn.result = (uc, fish3)
        if Turn.player1turn:
            Points.p1 += 3
        else:
            Points.p2 += 3
    
    elif num == 4:
        Turn.result = (uc, fish4)
        if Turn.player1turn:
            Points.p1 += 5
        else:
            Points.p2 += 5
    
    elif num == 5:
        Turn.result = (uc, fish5)
        if Turn.player1turn:
            Points.p1 += 10
        else:
            Points.p2 += 10
    
    else:
        Turn.result = (uc, "an electric eel! You have zero points and your Turn is over.")
        if Turn.player1turn:
            Points.p1 = 0
            Turn.switch = True
        else:
            Points.p2 = 0
            Turn.switch = True
    



