import random

# 20 lines of code. Each player has three turns per round.
fishing = True
while fishing == True:
    
    num = random.randint(1,6)

    uc = "You caught"

    # Round 3/3
    # Luke: 16
    # Johnny: 13

    # sock/fish/sock = double points
    # sock/sock/sock = safe from one electric eel

    fish1 = "a.. sock? +0"
    fish2 = "a plankter... +1"
    fish3 = "a catfish. +3"
    fish4 = "a giant squid! +5"
    fish5 = "a MEGALODON!!! +10"

    if num == 1:
        print(uc, fish1)
    elif num == 2:
        print(uc, fish2)
    elif num == 3:
        print(uc, fish3)
    elif num == 4:
        print(uc, fish4)
    elif num == 5:
        print(uc, fish5)
    else:
        print(uc, "an electric eel! You have zero points and your turn is over.")
        
        fishing = False
