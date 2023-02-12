# str, rpr, iter, next
from datetime import timedelta


class Book:
    def __init__(self, id: str, name: str, author: str, year_published: int, loan_time: int = 1):
        self._loan_time = loan_time
        self._year_published = year_published
        self._author = author
        self._name = name
        self._id = id

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_id(self):
        return self._id

    def get_year_published(self):
        return self._year_published

    def get_loan_time_duration(self):
        if self._loan_time == 1:
            return timedelta(days=10)
        if self._loan_time == 2:
            return timedelta(days=5)
        if self._loan_time == 3:
            return timedelta(days=2)

    def set_loan_time_duration(self, new_loan_time: int):
        if new_loan_time <= 3:
            self._loan_time = new_loan_time
            return True
        else:
            raise Exception("Invalid input, options are 1 / 2 / 3")

    def __str__(self):
        return f"{self._name}, by {self._author}, // Book ID: {self._id}"

    def __repr__(self):
        return self.__str__()
