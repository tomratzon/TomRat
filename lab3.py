'''
Create 2 variables : string of yout full name, another string of your mail.
Create variable of you age (int)

Then, print yout name from the end to the beginning and print it with age*3
then check if your full name is stourd inside the line:" tom dudu yuval ben idan dudu shimon ratzon"
'''
full_name=input("enter your full name: ")
mail=input("enter your mail: ")
age=input("enter your age: ")
print("your name backward is : "+full_name[::-1]+"\nyour age is: "+str(int(age)*3)+"\nyor mail is: "+mail+"\n")
if(full_name in "tom dudu yuval ben idan dudu shimon ratzon"):
    print(full_name+" IS in tom dudu yuval ben idan dudu shimon ratzon")
else:
    print(full_name+" IS NOT in tom dudu yuval ben idan dudu shimon ratzon")