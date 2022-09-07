'''

'''
from random import randint
print("Menu\n\n1) print 100 number\n2) check fibbo\n3) randint numbers until we get 12 or 10 numbers have been enters\n")
choice=input("enter your choice: ")
if(choice=="1"):
    for i in range(101):
        print((i))
elif(choice=="2"):
    num=input("enter a number for the series (x to end series) : ")
    ser1=[]
    while num!="x":
        ser1.append(int(num))
        num=input("enter a number for the series (3x to end series) : ")
    i=2
    while i <len(ser1):
       if(ser1[i]!=ser1[i-1]+ser1[i-2]):
           print("this is NOT a fibbonachi series!")
           break
       i+=1
    if(i==len(ser1)):
        print("this is a fibbonachi series!")
elif(choice=="3"):
    counter=0
    num=0
    while(counter<10 and num!=12):
        num=randint(1,12)
        print(num)
        counter+=1
else:
    print("not a valid choice")