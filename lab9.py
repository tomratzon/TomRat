
def dog_det():
    name=input("enter the dog name: ")
    age=input("enter the dog age: ")
    print("the dog "+name+" is "+str(float(age)*7)+" in dog yesrs")
def friend_list(list1):
    for i in range(5):
        friend_name=input("enter friend number "+str(i+1)+": ")
        list1.append(friend_name)
    name=input("choose any friend name: ")
    if(name in list1):
        print(name+" is in your friends list")
    else:
        print(name+" is not your friend!")

def n_azeret(num):
    new_num=1
    while int(num)!=0:
        new_num*=int(num)
        num-=1
    print(new_num)

def menu():
    print("MENU\n\n1) dog details\n2) friend list\n3)n!\n")
    choice = input("enter your choice: ")
    while True:

     if(choice=="1"):
         dog_det()
     elif (choice == "2"):
         list1=[]
         friend_list(list1)
     elif (choice == "3"):
         n_azeret(int(input("enter a number: ")))
     elif (choice == "x"):
         print("good bye...")
         break
     else:
          print("not a valid choice, choose again")
     print("MENU\n\n1) dog details\n2) friend list\n3)n!\n")
     choice = input("enter your choice: ")

menu()