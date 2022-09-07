list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4]
print(list1+list2)

print(list1+[9])
list3=["1","2","3","4","5"]
print("A".join(list3))   #combine list3 cells with "A" after every cell

str1="welcome to the library please be quiet"
print(str1.split())
list4=str1.split()
print(len(list4))  #len returns length of object as int type
list4.append("++")
print(list4) #add to the end of the list

list4.insert(5,"new word") #insert "new word" into index 5 and push the rest 0ne index forward
print(list4)
list4.pop()#delete the last cell of the list
print(list4)

