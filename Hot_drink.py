from Product import Product


class Hot_drink(Product):
    def __init__(self, name, price, volume, temperature):
        super().__init__(name, price)
        self._volume = volume
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @property
    def volume(self):
        return self._volume

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    def __str__(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Volume: {self.volume}, Temperature: {self.temperature}"

    def get_hot_drinks_list():
        hd_list = []

        hd1 = Hot_drink("Americano", 100, 100, 70)
        hd2 = Hot_drink("Americano", 200, 200, 80)
        hd3 = Hot_drink("Americano", 350, 400, 80)
        hd4 = Hot_drink("Black tea", 90, 100, 70)
        hd5 = Hot_drink("Black tea", 120, 200, 80)
        hd6 = Hot_drink("Black tea", 180, 400, 80)
        hd7 = Hot_drink("Green tea", 90, 100, 70)
        hd8 = Hot_drink("Green tea", 120, 200, 80)
        hd9 = Hot_drink("Green tea", 180, 400, 80)
        hd10 = Hot_drink("Hot chocolate", 140, 100, 80)
        hd11 = Hot_drink("Hot chocolate", 250, 200, 80)
        hd12 = Hot_drink("Latte", 200, 200, 60)
        hd13 = Hot_drink("Latte", 350, 400, 60)
        hd14 = Hot_drink("Americano", 250, 200, 80)

        hd_list.append(hd1)
        hd_list.append(hd2)
        hd_list.append(hd3)
        hd_list.append(hd4)
        hd_list.append(hd5)
        hd_list.append(hd6)
        hd_list.append(hd7)
        hd_list.append(hd8)
        hd_list.append(hd9)
        hd_list.append(hd10)
        hd_list.append(hd11)
        hd_list.append(hd12)
        hd_list.append(hd13)
        hd_list.append(hd14)

        return hd_list

    def get_list_of_available_drinks():
        all_drinks = ["black tea", "green tea",
                      "hot chocolate", "americano", "latte"]
        return all_drinks

    def get_list_of_available_volumes():
        all_volumes = [100, 200, 400]
        return all_volumes

    def get_list_of_available_temperatures():
        all_temperatures = [60, 70, 80]
        return all_temperatures

    def check_name():
        print(Hot_drink.get_list_of_available_drinks())
        name = input("Enter a hot drink name: ")

        while not name in Hot_drink.get_list_of_available_drinks():
            print('Wrong value, try again')
            name = input("Enter a hot drink name: ")
        return name

    def check_volumes():
        print(Hot_drink.get_list_of_available_volumes())
        volume = int(input("Enter a hot drink volume: "))

        while not volume in Hot_drink.get_list_of_available_volumes():
            print('Wrong value, try again')
            volume = int(input("Enter a hot drink volume: "))
        return str(volume)

    def check_temperatures():
        print(Hot_drink.get_list_of_available_temperatures())
        temperature = int(input("Enter a hot drink temperature: "))

        while not temperature in Hot_drink.get_list_of_available_temperatures():
            print('Wrong value, try again')
            temperature = int(input("Enter a hot drink temperature: "))
        return str(temperature)
