'''
create a list with 4 deatils abouth you : name,age,mail and phone. print it to the screen
then create another list with 2 IPs and add 3 more IPs, pop the 3rd IPand print how many IPs do we have and print them
'''
name=input("enter your name: ")
age=input("enter your age: ")
mail=input("enter your mail: ")
phone=input("enter your phone: ")
list_user=[name,age,mail,phone]
print(list_user)
print("\n")
ip_list=[]
ip_list.append(input("enter 1st IP: "))
ip_list.append(input("enter 2st IP: "))
ip_list.append(input("enter 3st IP: "))
ip_list.append(input("enter 4st IP: "))
ip_list.append(input("enter 5st IP: "))
print(ip_list)
ip_list.pop(2)
print(ip_list)
print("number of IPs that we have is: "+str(len(ip_list)))