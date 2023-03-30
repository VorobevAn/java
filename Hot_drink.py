from Product import Product


class Hot_drink(Product):

    def __init__(self, name, cost, temperature):
        super().__init__(name, cost)
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature

    def __str__(self) -> str:
        return f"{self._name} {self._cost} {self._temperature}"

