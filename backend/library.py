from backend.address import Address
from backend.book import Book
from backend.customer import Customer
from datetime import datetime, timedelta
from backend.loan import Loan


class Library:
    def __init__(self, library_name: str, library_address: Address):
        self._library_address = library_address
        self._library_name = library_name
        self._library_customers = {}
        self._library_books = {}
        self._loaned_books = {}
        self._loans_complete = {}
        self._late_loans = {}

    def add_new_customer(self, customer: Customer):
        customer_id = customer.get_id()
        if customer_id not in self._library_customers:
            self._library_customers[customer_id] = customer
            return True
        else:
            return False

    def remove_customer(self, customer: Customer):
        customer_id = customer.get_id()
        customer_loans = customer.display_active_loans()
        if customer_id in self._library_customers.keys() and len(customer_loans) == 0:
            del self._library_customers[customer_id]
            return True
        else:
            if customer_id not in self._library_customers.keys():
                print("We dont recognize that customer")
            elif len(customer_loans) > 0:
                print("That customer have active loans, handle it before removing him")
                return False

    def add_new_book(self, book: Book):
        book_id = book.get_id()
        if book_id not in self._library_books:
            self._library_books[book_id] = book
            return True

    def loan_book(self, book: Book, book_id: str, customer: Customer):
        # Checking if the book is not already taken or even exists
        if book_id not in self._library_books:
            raise Exception(f"The book id {book_id} is not on our shelf's")
        if book_id in self._loaned_books:
            raise Exception(f"The book is already loaned")
        # Pulling relevant info about the book and the loan
        loan_time = book.get_loan_time_duration()  # timedelta
        date_today = datetime.today()
        # Updating the library database
        loan_end_time = date_today + loan_time
        if loan_end_time.weekday() == 4:
            loan_end_time += timedelta(days=2)
        elif loan_end_time.weekday() == 5:
            loan_end_time += timedelta(days=1)
        loan = Loan(customer, book, date_today, loan_end_time)
        customer.add_loan(book)
        self._loaned_books[book_id] = loan
        self._library_books.pop(book_id)
        return True

    def return_book(self, book: Book, book_id: str, customer: Customer):
        if book_id not in self._loaned_books:
            raise Exception(f"{book} is not loaned. are you sure its ours? should i call the police?")
        self._loans_complete[datetime.now()] = \
            {customer.get_name(): Loan(customer.get_id(),
                                       book_id, self._loaned_books[book_id]["loan_start_time"], datetime.now())}
        if book_id in self._late_loans.keys():
            del self._late_loans[book_id]
        if book_id in self._loaned_books.keys():
            del self._loaned_books[book_id]
        self._library_books[book_id] = book
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

    def get_customer(self, customer_id: str):
        for key, value in self._library_customers.items():
            if key == customer_id:
                customer = value
                return customer

    def remove_book(self, book_id: str):
        book_id = book_id
        if book_id in self._library_books.keys() and book_id not in self._loaned_books.keys():
            del self._library_books[book_id]
            return True
        else:
            if book_id not in self._library_books.keys():
                print("We dont have that book, therefor we cant remove it")
            elif book_id in self._loaned_books.keys():
                print("That book is currently loaned, we cant remove it")
            return False

    def check_late_loans(self):
        for key, value in self._loaned_books.items():
            loan_id = key
            loan = value
            date_today = datetime.today()
            loan_end_time = loan.get_end_time()
            if date_today > loan_end_time:
                self._late_loans[loan_id] = loan
            else:
                continue
