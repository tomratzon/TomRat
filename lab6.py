from time import  sleep
text='''
Menu:
1)Insert Number and ** by 3
2)Insert 4 IPs to a list and print it
3)Insert 4 Enteries to DNS_Dictionary and peint it
4)Check if a string i s a Polyndrom
'''
ips=[]
flag=True
DNS_dictionary={}
choice=input(text+"\n")
if(choice == "1"):
    num=input("enter a number: ")
    print(str(num)+"**3 = "+str(float(num)**3))
elif(choice=="2"):
        ips.append(input("enter 1st IP: "))
        ips.append(input("enter 2nd IP: "))
        ips.append(input("enter 3rd IP: "))
        ips.append(input("enter 4th IP: "))
        print("................")
        print(ips)
        print("................")
elif(choice=="3"):
    addr=input("enter 1st DNS address: ")
    val=input("enter value: ")
    DNS_dictionary[addr]=val
    addr = input("enter 2nd DNS address: ")
    val = input("enter value: ")
    DNS_dictionary[addr] = val
    addr = input("enter 3rd DNS address: ")
    val = input("enter value: ")
    DNS_dictionary[addr] = val
    addr = input("enter 4th DNS address: ")
    val = input("enter value: ")
    DNS_dictionary[addr] = val
    print("................")
    print(DNS_dictionary)
    print("................")
elif(choice=="4"):
    str1=input("enter your string: ")
    for i in range(len(str1)//2):
        if(str1[i]!=str1[len(str1)-1-i]):
            print(str1+" is not a Polyndrom")
            flag=False
            break
    if(flag==True):
        print(str1+" is a Polyndrom")
else:
    print("invalid .... 1-4 only")

