from Vending_machine import *
from Product import Product
from Hot_drink import*

product1 = Product("pepsi", 30)
product2 = Hot_drink("чай", 20, 80)

mylist = Vendig_machine()
mylist.add_list(product1)
mylist.add_list(product2)
Vendig_machine.print(mylist)

vendig = Vendig_machine()

print(vendig.get_product("pepsi", 30))


