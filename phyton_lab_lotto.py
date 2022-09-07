from random import randint
print("WELCOM")
'''
budget=input("enter you budget: ")
#facebook campaign =100 ILS per day
#instegram campaign =50 ILS per day
fb_length=input("how long (in days) do you want the facebook campaign to operate? ")
ins_length=input("how long (in days) do you want the instegram campaign to operate? ")
total=((int(fb_length)*100)+(int(ins_length)*50))*0.17
print("total cost with 17% tax will be "+str(total)+"\n")
if(total>int(budget)):
    print("you need to add "+str(total-int(budget))+" ILS")
else:
    print("sucsessful")
'''
def lottory():
    win_list=[]
    while(len(win_list)<6):
        num=randint(1,37)
        if(num not in win_list):
            win_list.append(num)
    return  win_list

money=input("each game cost 3 ILS, insert the amount of money you have: ")
#each game cost 4 ILS
round_counter=0
money_won=0
counter=0
win_list=lottory()
print(win_list)
while(int(money)>0):
    my_numbers=lottory()
    print(my_numbers)
    for i in range(len(my_numbers)):
        if(my_numbers[i] in win_list):
            counter+=1
    if(counter==6):
        print("you won 1,000,000 ILS!!\n")
        money_won+=1000000
    elif (counter == 5):
        print("you won 1,000,000 ILS!!\n")
        money_won += 5000
    elif (counter == 4):
        print("you won 1,000,000 ILS!!\n")
        money_won += 100
    elif (counter == 3):
        print("you won 1,000,000 ILS!!\n")
        money_won += 10
    else:
        print("you lost!\n")
    money=int(money)-3
    counter=0
    print("curr game money is "+str(money)+" ILS\n")
print("total money won is "+str(money_won))



