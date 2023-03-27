from Vending_machine import Vending_machine


class Vending_machine_hot_drinks(Vending_machine):

    def __init__(self, list):
        super().__init__(list)

    def get_product(self, name, volume, temperature):
        chosen_list = []

        for el in self._list:
            if str(name).lower() in str(el).lower() and volume in str(el) and temperature in str(el):
                chosen_list.append(el)
        return chosen_list
