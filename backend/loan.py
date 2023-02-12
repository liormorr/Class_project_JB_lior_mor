from datetime import datetime, timedelta

from backhand.book import Book


class Loan:
    def __init__(self, customer_id: str, book_id , loan_date: datetime, return_date: datetime):
        self._return_date = return_date
        self._loan_date = loan_date
        self._book_id = book_id
        self._customer_id = customer_id

    def get_customer_id(self):
        return self._customer_id

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



