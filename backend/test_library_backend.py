import datetime
import unittest

from backend.address import Address
from backend.book import Book
from backend.customer import Customer
from backend.loan import Loan
from backend.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library_address = Address("Kfar Yona", "Ahavat Adam", 79)
        self.library = Library("Saint Lior's Regional Community Library", self.library_address)
        self.book_test = Book("tkam1", "To Kill a MockingBird", "Harper Lee", 1960)
        self.book_test2 = Book("ak1", "Anna Karenina", "Leo Tolstoy", 1878)
        self.customer_address = Address("Kfar Yona", "Ahavat Adam", 79)
        self.customer = Customer("lm1", "Lior", "Mor", self.customer_address, "liormorr@gmail.com", "4.9.90")

    print("--- Starting Library Tests ---")

    def test_add_book(self):
        self.assertTrue(Library.add_new_book(self.library, self.book_test), True)
        self.assertFalse(Library.add_new_book(self.library, self.book_test), False)

    def test_return_book(self):
        self.assertFalse(Library.return_book(self.library, self.book_test2, self.book_test2.get_id(), self.customer))
        self.library.add_new_book(self.book_test2)
        self.library.add_new_book(self.book_test)
        self.assertFalse(Library.return_book(self.library, self.book_test, self.book_test.get_id(), self.customer))
        self.library.loan_book(self.book_test, self.book_test.get_id(), self.customer)
        self.assertTrue(Library.return_book(self.library, self.book_test, self.book_test.get_id(), self.customer))

    def test_remove_book(self):
        self.library.add_new_book(self.book_test)
        self.assertTrue(Library.remove_book(self.library, self.book_test.get_id()))
        self.assertFalse(Library.remove_book(self.library, self.book_test2.get_id()))

    def test_loan_book(self):
        self.library.add_new_book(self.book_test)
        self.assertTrue(Library.loan_book(self.library, self.book_test, self.book_test.get_id(), self.customer))
        self.assertFalse(Library.loan_book(self.library, self.book_test2, self.book_test2.get_id(), self.customer))

    print("--- Library Tests Finished ---")


class TestCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.customer_address = Address("Kfar Yona", "Ahavat Adam", 79)
        self.customer = Customer("lm1", "Lior", "Mor", self.customer_address, "liormorr@gmail.com", "4.9.90")
        self.book_test = Book("tkam1", "To Kill a MockingBird", "Harper Lee", 1960)

    print("--- Starting Customer Tests ---")

    def test_customer_class(self):
        self.assertTrue(Customer.get_id(self.customer), "lm1")
        self.assertTrue(Customer.get_name(self.customer), "Lior Mor")
        self.assertTrue(Customer.get_email(self.customer), "liormorr@gmail.com")
        self.assertTrue(Customer.get_birthday(self.customer), "04-09-1990")
        self.assertTrue(Customer.get_address(self.customer), "Kfar Yona, Ahavat Adam street, Number: 79")
        self.assertIsNone(Customer.add_loan(self.customer, self.book_test))

    print("--- Customer Tests Finished ---")


class TestLoan(unittest.TestCase):
    def setUp(self) -> None:
        self.customer_address = Address("Kfar Yona", "Ahavat Adam", 79)
        self.customer = Customer("lm1", "Lior", "Mor", self.customer_address, "liormorr@gmail.com", "4.9.90")
        self.book_test = Book("tkam1", "To Kill a MockingBird", "Harper Lee", 1960)
        self.end_time_test = datetime.datetime.now() + datetime.timedelta(days=3)
        self.loan = Loan(self.customer, self.book_test, datetime.datetime.now(), self.end_time_test)

    print("--- Starting Loan Tests ---")

    def test_loan_class(self):
        self.assertTrue(Loan.get_customer_id(self.loan), "lm1")
        self.assertTrue(Loan.get_loan_date(self.loan), datetime.datetime.now())
        self.assertTrue(Loan.get_end_time(self.loan), self.end_time_test)
        self.assertIsNone(Loan.set_return_date(self.loan, datetime.datetime.now()))

    print("--- Loan Tests Finished ---")


class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.book_test = Book("tkam1", "To Kill a MockingBird", "Harper Lee", 1960, loan_time=3)

    print("--- Starting Book Tests ---")

    def test_book_class(self):
        self.assertTrue(Book.get_id(self.book_test), "tkam1")
        self.assertTrue(Book.get_name(self.book_test), "To Kill a MockingBird")
        self.assertTrue(Book.get_author(self.book_test), "Harper Lee")
        self.assertTrue(Book.get_loan_time_duration(self.book_test), datetime.timedelta(days=2))
        self.assertTrue(Book.get_year_published(self.book_test), 1960)
        self.assertTrue(Book.set_loan_time_duration(self.book_test, 1), datetime.timedelta(days=10))

    print("--- Book Tests Finished ---")


if __name__ == '__main__':
    unittest.main()
