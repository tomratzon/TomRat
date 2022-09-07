#1
print("Twinkle, twinkle, little star,\n      How I wonder what you are!\n            Up above the world so high, \n            Like a diamond in the sky. \nTwinkle, twinkle, little star, \n      How I wonder what you are")
#8
'''
color_list=["Red","Green","White","Black"]
print("the forst color is: "+color_list[0])
print("the last color is: "+color_list[len(color_list)-1])
'''
#10
'''
num=input("enter an integer: ")
sum=int(num)+int(num*2)+int(num*3)
print("output: "+str(sum))
'''
#18
'''
num1=input("enter 1st number: ")
num2=input("enter 2nd number: ")
num3=input("enter 3rd number: ")
if(num1==num2 and num2==num3):
    print("output: "+str((float(num1)*3)*3))
else:
    print("output: "+str(float(num1)+float(num2)+float(num3)))
'''
#34
'''
num1=input("enter 1st number: ")
num2=input("enter 2nd number: ")
sum=float(num1)+float(num2)
if(sum>=15 and sum<=20):
    print("output: 20")
else:
    print("output: "+str(sum))
'''
#37
'''
name=input("enter your name: ")
age=input("enter your age: ")
addr=input("enter your address: ")
print("yout name is "+name+"\nyou are "+str(age)+" years old\n your address is "+addr)
'''
#38
'''
x=input("enter x: ")
y=input("enter y: ")
sol=(float(x)+float(y))*(float(x)+float(y))
print("output: "+str(sol))
'''
#59
'''
height=input("enter height in feet and inches: ")
feet=inches=height.split(".",1)[0]
inches=height.split(".",1)[1]
conv_h=int(feet)*30.48+int(inches)*2.54
print(" the height in cm is: "+str(conv_h)+" cm")
'''
#94
'''
byte_str=input("enter binary seq: ")
num=0
for i in range(len(byte_str)):
    if(int(byte_str[i])==1):
        num+=2**(len(byte_str)-1-i)

print("the number is "+str(num))
'''


#149
def sum_of_int(num):
    sum=0
    for i in range(int(num)):
        sum+=i**2
    return sum
print("output: "+str(sum_of_int(input("enter an integer: "))))
