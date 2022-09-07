'''
Prices:
tometos: 3 nis per unit
cucumbers: 2 nis per unit
cola: 5 nis
chicken: 20 nis per kilo
VAT= 17%

program recieve quantities from user and calculate the total price with VAT and without VAT
'''
print("Prices:\ntometos: 3 nis per unit\ncucumbers: 2 nis per unit\ncola: 5 nis\nchicken: 20 nis per kilo\nVAT= 17%\n")
tomatos=input("enter how many tomestos you would like to buy: ")
cucumber=input("enter how many cucumber you would like to buy: ")
cola=input("enter how many cola bottles you would like to buy: ")
chicken=input("enter how many kilos of chicken you would like to buy: ")

novat=(3*int(tomatos)+2*int(cucumber)+5*int(cola)+20*int(chicken))

print("\ntotal price is : "+str(novat)+" whitout VAT")
print("                 "+str("%.2f"%(novat*1.17))+" after VAT")

