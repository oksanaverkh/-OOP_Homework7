# 1. Создать наследника реализованного класса ГорячийНапиток с дополнительным полем int температура.
# 2. Создать класс ГорячихНапитковАвтомат реализующий интерфейс ТорговыйАвтомат
# и реализовать перегруженный метод getProduct(int name, int volume, int temperature) выдающий продукт соответствующий имени, объему и температуре
# 3. В main проинициализировать несколько ГорячихНапитков и ГорячихНапитковАвтомат и воспроизвести логику заложенную в программе
# 4. Все вышеуказанное создать согласно принципам ООП пройдённым на семинаре

from Hot_drink import *
from Vending_machine_hot_drinks import *

import os
os.system('cls')


def main():

    hot_drinks_list = Vending_machine_hot_drinks(
        Hot_drink.get_hot_drinks_list())

    name = Hot_drink.check_name()
    print()

    volume = Hot_drink.check_volumes()
    print()

    temperature = Hot_drink.check_temperatures()
    print()

    final_list = Vending_machine_hot_drinks(
        hot_drinks_list.get_product(name, volume, temperature))

    if final_list.is_empty() == False:
        print("Available drinks:")
        final_list.print()

    else:
        print("No available drinks")


if __name__ == "__main__":
    main()
