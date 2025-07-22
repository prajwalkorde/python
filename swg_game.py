'''snack - 1
   water - -1
   gun   - 0'''
import random
#comp and player choice generater.
youdic = {"snack" : 1, "water": -1, "gun" : 0}
cpdic = {1:"snack", -1:"water", 0:"gun"}
n=input("enter your choice: ")
you = youdic[n]
comp= random.choice([-1,0,1])
#print choices.
print(f"you choose {n}\ncomputer choose {cpdic[comp]}")
#possible outcomes of game.
if(you == comp):
    print("its a draw.")
else:
    if(comp==1 and you==-1):
        print("You Loose!")
    elif(comp==1 and you==0):
        print("You Win!")
    elif(comp==0 and you==-1):
        print("You Win!")
    elif(comp==0 and you==1):
        print("You Loose!")
    elif(comp==-1 and you==1):
        print("You Win!")
    elif(comp==-1 and you==0):
        print("You Loose!")
    else:
        print("something went wrong.")

