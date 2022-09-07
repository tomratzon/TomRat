num =4567

print("alaphim: "+str(int(num//1000)))
print("meot: "+str(int((num//100)-((num//1000))*10)))
print("asarot: "+str(int((num//10)-((num//100)*10))))
print("yehisdot: "+str(int(num-((num//10)*10))))