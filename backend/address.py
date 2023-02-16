class Address:
    def __init__(self, city: str, street: str, num: int, level=None, apartment_num=None):
        self._apartment = apartment_num
        self._level = level
        self._num = num
        self._street = street
        self._city = city

    def get_city(self):
        return self._city

    def get_street(self):
        return self._city

    def get_house_info(self):
        if self._level is not None:
            return self._num, self._level
        if self._level is not None and self._apartment is None:
            return self._num, self._level, self._apartment
        else:
            return self._num

    def set_city(self, new_city: str):
        self._city = new_city

    def set_street(self, new_street: str):
        self._street = new_street

    def set_house_num(self, new_house_num: int):
        self._num = new_house_num

    def __str__(self):
        return f"{self._city}, {self._street} street, Number: {self._num}"
