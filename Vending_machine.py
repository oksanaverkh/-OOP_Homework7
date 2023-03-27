from Product import *
from Hot_drink import *


class Vending_machine():

    def __init__(self, list):
        self._list = list

    def get_product(self, product):
        for el in self._list:
            if str(el).lower() == product:
                print(el)

    def print(self):
        for el in self._list:
            print(str(el))

    def is_empty(self):
        if not self._list:
            return True
        else:
            return False
