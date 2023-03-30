class Product():

    def __init__(self, name, cost):
        self._name = name
        self._cost = cost



    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost


    @name.setter
    def name(self, new_neme):
        self._name = new_neme

    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost



    def __str__(self) -> str:
        return f"{self._name} {self._cost}"

