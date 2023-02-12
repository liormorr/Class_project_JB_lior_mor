from datetime import datetime, timedelta

from backend.book import Book
from backend.customer import Customer


class Loan:
    def __init__(self, customer: Customer, book: Book, loan_date: datetime, loan_end_time: datetime):
        self._return_date = None
        self._loan_date = loan_date
        self._customer = customer
        self._book_name = book.get_name()
        self._loan_end_time = loan_end_time

    def get_customer_id(self):
        return self._customer.get_id()

    def get_loan_date(self):
        return self._loan_date

    def get_return_date(self):
        return self._return_date

    def update_return_date(self, time_in_days: int, add=True):
        if add is True:
            self._return_date = self._return_date + timedelta(days=time_in_days)
            return True
        if add is False:
            self._return_date = self._return_date - timedelta(days=time_in_days)
            return True

    def get_end_time(self):
        return self._loan_end_time

    def set_return_date(self, return_date):
        pass

    def __repr__(self):
        time = datetime.strftime(datetime.now(), "%d/%m/%Y")
        end_time = datetime.strftime(self._loan_end_time, "%d/%m/%Y")
        return f"name: {self._book_name}, Loan started: {time}, Loan should end by: {end_time}, " \
               f"Loaned by {self._customer}"
