import random


uc = "You caught"

fish1 = "a.. sock? +0"
fish2 = "a plankter... +1"
fish3 = "a catfish. +3"
fish4 = "a giant squid! +5"
fish5 = "a MEGALODON!!! +10"

x=0
class turn:
    result = ""

def fish():    
    num = random.randint(1,6)
    p1=0
    p2=0

    if num == 1:
        turn.result = (uc, fish1)
    
    elif num == 2:
        turn.result = (uc, fish2)
        if x == 0:
            p1 += 1
        else:
            p2 += 1
        
    elif num == 3:
        turn.result = (uc, fish3)
        if x == 0:
            p1 += 3
        else:
            p2 += 3
    
    elif num == 4:
        turn.result = (uc, fish4)
        if x == 0:
            p1 += 5
        else:
            p2 += 5
    
    elif num == 5:
        turn.result = (uc, fish5)
        if x == 0:
            p1 += 10
        else:
            p2 += 10
    
    else:
        turn.result = (uc, "an electric eel! You have zero points and your turn is over.")
        if x == 0:
            p1 = 0
        else:
            p2 = 0
    



