from backend.address import Address
import re

from backend.book import Book


class Customer:
    def __init__(self, id: str, first_name: str, last_name: str, address: Address, email: str, birthday: str):
        self._birthday = birthday
        self._email = email
        self._address = address
        self._name = f"{first_name} {last_name}"
        self._id = id
        self._loaned_books = {}

    def get_birthday(self):
        return self._birthday

    def get_email(self):
        return self._email

    def get_address(self):
        return self._address

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def set_email(self, new_email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, new_email):
            self._email = new_email
            return True
        else:
            raise Exception("Invalid mail, please try again")

    def add_loan(self, book: Book):
        book_id = book.get_id()
        self._loaned_books[book_id] = book

    def display_active_loans(self):
        return self._loaned_books

    def __str__(self):
        return f"Customer name: {self._name}, Customer ID: {self._id}"

    def __repr__(self):
        return f"Customer name: {self._name}, Customer ID: {self._id}, Customer Address: {self._address}"
