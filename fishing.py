import random

# 20 lines of code. Each player has three turns per round.

imp = int(input("How many rounds would you want to play?"))


fishing = True
    
p1 = 0
p2 = 0

for y in range(imp):
    for x in range(2):
        
        if x == 0:
            print("Player 1")
            
        else:
            print("Player 2")
            
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
                fishing = False
            elif num == 2:
                print(uc, fish2)
                if x == 0:
                    p1 += 1
                else:
                    p2 += 1
                fishing = False
            elif num == 3:
                print(uc, fish3)
                if x == 0:
                    p1 += 3
                else:
                    p2 += 3
                fishing = False
            elif num == 4:
                print(uc, fish4)
                if x == 0:
                    p1 += 5
                else:
                    p2 += 5
                fishing = False
            elif num == 5:
                print(uc, fish5)
                if x == 0:
                    p1 += 10
                else:
                    p2 += 10
                fishing = False
            else:
                print(uc, "an electric eel! You have zero points and your turn is over.")
                if x == 0:
                    p1 = 0
                else:
                    p2 = 0
                fishing = False
                
                
            print("Player 1:",p1,"Player 2:",p2)
               
            if num == 6:
                pass
            else:
                inp = input("fish or stop?")
                if inp == "fish":
                    fishing = True
                else:
                    fishing = False


if p1 > p2:
    print("Player 1 wins!")
elif p2 > p1:
    print("Player 2 wins!")
else:
    print("It's a draw!")

