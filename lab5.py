'''
create a dictionary with 5 names & money
then sum the money of the first & last name and print it to the screen
after, add new name with the sum of money you calculated before in the end of the dictionary and print then umber of enteries
and check if "tom" is inside the dictionary
'''
new_dic={}
for i in range(5):
    name=input("enter name : ")
    money=input("enter sum of money:")
    new_dic.update({name:money})
new_sum = float(list(new_dic.values())[0])+float(list(new_dic.values())[len(new_dic)-1])
print("the sum of the fitst person money and last pperson money is: "+str(new_sum))
new_name=input("enter a new name please: ")
new_dic.update({new_name:new_sum})
print("the number of enteries is: "+str(len(new_dic)))
print("is \"tom\" in the dictionary?\n")
print("tom" in new_dic.keys())
