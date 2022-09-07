import  datetime
from time import  sleep
#1
print("Net4U, is the best place…\n     in the world")
#2
print("current time and date : "+str(datetime.datetime.now()))
#3
'''
f_name=input("enter your first name: ")
l_name=input("enter your last name: ")
print("your reversed name is: "+str(l_name[::-1])+" "+str(f_name[::-1]))
'''
#4
'''
file_name=input("enter the file name: ")
print(" file type : "+file_name.split(".",1)[1])
'''
#5
'''
num=input("please enter an number between 0 to 9: ")
print(num+"+"+num*2+"+"+num*3+"= "+str(int(num)+int(num*2)+int(num*3)))
'''
#6
'''
num=input("enter a number: ")
if(int(num)%2==0):
    print("the number is even")
else:
    print("the number odd")
'''
#7
'''
height=input("enter height in feet and inches: ")
feet=inches=height.split(".",1)[0]
inches=height.split(".",1)[1]
conv_h=int(feet)*30.48+int(inches)*2.54
print(" the height in cm is: "+str(conv_h)+" cm")
'''
#8
'''
dic1={}
key1=input("enter a key: ")
val1=input("enter a value: ")
dic1[key1]=val1
print(dic1)
dic1.pop(key1);
print("deleting...")
sleep(3)
print(dic1)
'''
#9
'''
dic1={0: 10, 1: 20}
print(dic1)
key1=input("enter a key: ")
val1=input("enter a value: ")
dic1[key1]=val1
print(dic1)
'''
#10
'''
str1=input("enter your string: ")
dic1={}
for i in range(len(str1)):
    dic1[str1[i]]=1
print(dic1)
'''
#11
'''
str1=input("enter your string1: ")
str2=input("enter your string2: ")
char1=str1[0]
char2=str2[0]
str1=char2+str1[1:]
str2=char1+str2[1:]
str3=str1+" "+str2
print(str3)
'''
#12
'''
str1=input("enter your string: ")
dic1={}
for i in range(len(str1)):
    if(str1[i] in dic1):
        dic1[str1[i]]+=1
    else:
        dic1[str1[i]] = 1
print(dic1)
'''
#13
'''
list1=[]
sum=0
item=input("enter a number (.) to exit : ")
while item!=".":
    list1.append(float(item))
    item = input("enter a number (.) to exit : ")
for i in range(len(list1)):
    sum+=list1[i]
print(sum)
'''
#14
list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index_list=[]
idx=input("enter an index (.) to exit : ")
while idx!=".":
    index_list.append(int(idx))
    idx = input("enter a number (.) to exit : ")

for i in range(len(index_list)):
    list1.pop(index_list[i]-i)
print(list1)
