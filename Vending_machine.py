from Product import*
from Hot_drink import Hot_drink

class Vendig_machine():

    def __init__(self):
        list = []
        self._list = list

    def add_list(self, list_product):
        self._list.append(list_product)

    def get_product(self, name, cost):
        for i in self._list:
            if self._list[i] == name:
                return i
        return Product("Товар не найден", 0)

    def print(self):
        for i in self._list:
            print(str(i))
