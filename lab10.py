#lab10
def IP_menu(ip_list):
    choice=0
    counter=0
    while choice!="x":
        print("\nIP MENU\n\n1) serch for IP address from the list\n2) add IP address to the list\n3) delete IP address from the list\n4) print all IPs")
        choice = input("enter choice (x to Main Menu): ")
        if(choice=="1"):
            ip1=input("enter IP address for search: ")
            if(ip1 in ip_list):
                print(ip1+" is in the list\n")
            else:
                print(ip1+" isn't in the list\n")
        elif (choice == "2"):
            ip1 = input("enter IP address to add: ")
            ip_list.append(ip1)
        elif (choice == "3"):
            ip1 = input("enter IP address to delete: ")
            for i in range(len(ip_list)):
                if(ip1==ip_list[i-counter]):
                    ip_list.pop(i)
                    counter+=1
        elif (choice == "4"):
            for i in range(len(ip_list)):
                print(ip_list[i])
        elif (choice != "x"):
            print("not a valid choice, choose again")
    main_menu(ip_list,url_dic)



def DNS_menu(url_dic):
    choice = 0
    while choice != "x":
        print("\nURL MENU\n\n1) serch for URL  in a dictionary\n2) add URL to a dictionary\n3) delete URL from a dictionary\n4) update the IP address of specific URL\n5) print all URL:IP to screen")
        choice = input("enter choice (x to Main Menu): ")
        if (choice == "1"):
            url1 = input("enter URL address for search: ")
            if ( url1 in url_dic):
                print(url1 + " is in the dictionary\n")
            else:
                print(url1 + " isn't in the dictionary\n")
        elif (choice == "2"):
            url1 = input("enter URL address to add: ")
            url_dic[url1]=""
        elif (choice == "3"):
            url1 = input("enter URL address to delete: ")
            url_dic.pop(url1)
        elif (choice == "4"):
            url1 = input("enter URL address to update: ")
            ip1=input("enter ip address: ")
            url_dic[url1]=ip1
        elif (choice == "5"):
            print(url_dic)
        elif (choice != "x"):
            print("not a valid choice, choose again")
    main_menu(ip_list,url_dic)

def main_menu(ip_list,url_dic):
    choice=0
    while choice!="x":
        print("\nMENU\n\na) IP System\nb) DNS System")
        choice = input("enter choice: ")
        if(choice=="a"):
            IP_menu(ip_list)
        elif(choice=="b"):
            DNS_menu(url_dic)
        elif(choice!="x"):
            print("not a valid choice, choose again")

ip_list=[]
url_dic={}
main_menu(ip_list,url_dic)