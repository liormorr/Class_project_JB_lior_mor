from backhand.address import Address
from backhand.book import Book
from backhand.customer import Customer
from datetime import datetime, timedelta
from backhand.loan import Loan
import pickle


class Library:
    def __init__(self, library_name: str, library_address: Address):
        self._library_address = library_address
        self._library_name = library_name
        self._library_customers = {}
        self._library_books = {}
        self._loaned_books = {}
        self._loans_complete = {}
        self._late_loans = {}
        self._loan_end_time = None

    def add_new_customer(self, customer: Customer):
        customer_id = customer.get_id()
        if customer_id not in self._library_customers:
            self._library_customers[customer_id] = customer
            return True
        else:
            return False

    def add_new_book(self, book: Book):
        book_id = book.get_id()
        if book_id not in self._library_books:
            self._library_books[book_id] = book

    def loan_book(self, book: Book, book_id: str, customer: Customer):
        # Checking if the book is not already taken or even exists
        if book_id not in self._library_books:
            raise Exception(f"The book id {book_id} is not on our shelf's")
        if book_id in self._loaned_books:
            raise Exception(f"The book is already loaned, should be available at {self._loan_end_time}")
        # Pulling relevant info about the book and the loan
        loan_time = book.get_loan_time_duration()  # timedelta
        date_today = datetime.today()
        # Updating the library database
        self._loan_end_time = date_today + loan_time
        if self._loan_end_time.weekday() == 4:
            self._loan_end_time += timedelta(days=2)
        elif self._loan_end_time.weekday() == 5:
            self._loan_end_time += timedelta(days=1)
        self._loaned_books[book_id] = {"name": book, "loan_start_time": date_today,
                                       "loan_end_time": self._loan_end_time, "customer_loaned": customer}
        self._library_books.pop(book_id)

    def return_book(self, book: Book, book_id: str, customer: Customer):
        if book_id not in self._loaned_books:
            raise Exception(f"{book} is not loaned. are you sure its ours? should i call the police?")
        self._loans_complete[datetime.now()] = \
            {customer.get_name(): Loan(customer.get_id(),
                                       book_id, self._loaned_books[book_id]["loan_start_time"], datetime.now())}
        del self._loaned_books[book_id]
        self._library_books[book_id] = book
        self._loan_end_time = None
        return True

    def display_books(self):
        return self._library_books

    def display_customers(self):
        return self._library_customers

    def display_loans(self):
        return self._loaned_books

    def display_late_loans(self):
        return self._late_loans

    def get_name(self):
        return self._library_name

    def remove_book(self, book_id: str):
        book_id = book_id
        if book_id in self._library_books.keys():
            del self._library_books[book_id]
            return True
        else:
            return False
