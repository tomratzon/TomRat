from random import randint
from time import sleep
'''
game cost : 3 NIS
'''
mon=input("how much money do you have to play? \n")
print("game will cost 3 NIS")
play=input("enter x to play: ")
if(play=="x"):
    mon = (int(mon) - 3)
    print("...")
    sleep(1)
    print("..")
    sleep(1)
    print(".")
    sleep(1)
    print("you now have "+str(mon)+" NIS")
    sleep(1)
    print("dices are rolling...")
    sleep(1)
    print("dices are rolling..")
    sleep(1)
    print("dices are rolling.")
    sleep(1)
    dice1=randint(1,6)
    dice2=randint(1,6)
    print("your results are ["+str(dice1)+","+str(dice2)+"]\n")
    if(dice1==dice2):
        if(dice1==6):
            print("Congratulation, you won 1000 NIS")
            mon=(int(mon)+1000)
        else:
            print("Congratulation, you won 100 NIS")
            mon = (int(mon) + 100)
    else:
        if(dice2==2):
            print("Congratulation, you won 40 NIS")
            mon = (int(mon) + 40)
        elif(dice1==1):
            print("Congratulation, you won 100 NIS")
            mon = (int(mon) + 20)
        else:
            print("sorry you lost")
    print("you now have "+str(mon)+" NIS")
else:
        print("Good Bye...")