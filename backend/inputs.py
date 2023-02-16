import pickle
import re

from backend.address import Address
from backend.book import Book
from backend.customer import Customer
from backend.exceptions import *
from backend.library import Library
from backend.loan import Loan


def choice_confirmation(confirmation: str):
    possible_choices = ("1", "2", "$")
    if confirmation not in possible_choices:
        raise InvalidInput
    else:
        return True


def check_book_id(book_id: str, library: Library):
    books = library.display_books()
    if book_id not in books.keys():
        raise InvalidBookID
    else:
        return True


def set_birthday_for_customer():
    while True:
        birth_day = input("Please insert your birth date (DD-MM-YYYY): ")
        if not re.search('^[0-3][0-9]-[0-3][0-9]-(?:[0-9][0-9])?[0-9][0-9]$', birth_day):
            raise BirthDayError
        else:
            return birth_day


def set_email_for_customer():
    while True:
        email = input("Please insert your email: ")
        if not re.search('[a-z0-9]+@[a-z]+\.[a-z]{2,3}', email):
            raise EmailError
        else:
            return email


def set_id_for_customer(library: Library):
    print("ID should contain at least 2 letters and preferably at least 1 number at the end")
    id_for_customer = input("Please Enter your desired ID: ")
    if id_for_customer in library.display_customers().keys():
        raise CustomerIDExists
    if not re.search("^[a-zA-Z]{2,}[0-9_]+$", id_for_customer):
        raise CustomerIDError
    else:
        return id_for_customer


def set_first_name():
    while True:
        first_name = input("Please enter your first name: ")
        if not first_name.isalpha():
            raise InvalidInput("Error, name should contain only letters")
        if len(first_name) < 2:
            raise InvalidInput("Error, name should have more than 1 letter")
        else:
            first_name = first_name.title()
            return first_name


def set_last_name():
    while True:
        last_name = input("Please enter your last name: ")
        if not last_name.isalpha():
            raise InvalidInput("Error, name should contain only letters")
        if len(last_name) < 2:
            raise InvalidInput("Error, name should have more than 1 letter")
        else:
            last_name = last_name.title()
            return last_name


# def full_name():
#     while True:
#         first_name = input("Please enter your first name: ")
#         if not first_name.isalpha():
#             print("Error, name should contain only letters")
#             continue
#         if len(first_name) < 2:
#             print("Error, name should have more than 1 letter")
#             continue
#         break
#     while True:
#         last_name = input("Please enter your last name: ")
#         if not last_name.isalpha():
#             print("Error, last name should contain only letters")
#             continue
#         if len(last_name) < 2:
#             print("Error, last name should have more than 1 letter")
#             continue
#         break
#     name = first_name.title() + " " + last_name.title()
#     return name


def set_city_address():
    while True:
        city = input("Please enter the name of your city: ")
        if not re.search("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", city):
            raise AddressError("Error, city should contain only letters")
        if len(city) < 2:
            raise AddressError("Error, city should have more than 1 letter")
        else:
            city = city.title()
            return city


def set_street_address():
    while True:
        street = input("Please enter the name of your street: ")
        if not re.search("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", street):
            raise AddressError("Error, invalid street input")
        if len(street) < 2:
            raise AddressError("Error, street should have more than 1 letter")
        else:
            street = street.title()
            return street


def set_house_number_address():
    while True:
        house_number = input("Please enter the number of your house: ")
        if not house_number.isdigit():
            raise AddressError("Error, house number should contain only numbers")
        else:
            house_number = int(house_number)
            return house_number


def set_level_address():
    while True:
        level = input("Please enter the number of your level: ")
        if not level.isdigit():
            raise AddressError("Error, level should contain only numbers")
        else:
            return level


def set_apartment_num_address():
    while True:
        apartment_num = input("Please enter the number of your apartment: ")
        if not apartment_num.isdigit():
            raise AddressError("Error, apartment number should contain only numbers")
        else:
            return apartment_num


def set_book_name_for_register():
    while True:
        book_name = input("Please enter the Book's name: ")
        if not re.search("[A-Za-z]?", book_name):
            raise BookInsertionError("Invalid name, please try again")
        else:
            return book_name


def set_book_id_for_register(library: Library):
    while True:
        book_id = input("Please type the book ID: ")
        if not re.search("^[a-zA-Z]{2,}[0-9]*$", book_id):
            raise BookInsertionError
        if book_id in library.display_books().keys():
            raise InvalidBookID
        else:
            return book_id


def search_book_author():
    while True:
        book_author = input("Please type the book author name: ")
        if not re.search("^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$", book_author):
            raise InvalidInput
        else:
            book_author = str(book_author)
            return book_author.title()


def set_book_author_for_register():
    while True:
        book_author = input("Please type the book author name: ")
        if not re.search("^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$", book_author):
            raise BookInsertionError("Invalid author name, please try again")
        else:
            return book_author


def set_year_published_for_register():
    while True:
        year_published = input("Please enter the year the book published: ")
        if not re.search("^[12][0-9]{3}$", year_published):
            raise BookInsertionError("Invalid year entered, please try again")
        else:
            return year_published


def set_loan_time_for_register():
    while True:
        loan_time_options = ("1", "2", "3")
        loan_time_typed = input("'1' means up 10 days\n'2' means up to 5 days\n'3' means up to 2 days\n"
                                "Please enter the loan time for the book: ")
        if loan_time_typed not in loan_time_options:
            raise BookInsertionError("Invalid input")
        else:
            loan_time_typed = int(loan_time_typed)
            return loan_time_typed


def customer_from_input(library: Library):
    first_name = set_first_name()
    last_name = set_last_name()
    id = set_id_for_customer(library)
    email = set_email_for_customer()
    birth_day = set_birthday_for_customer()
    city = set_city_address()
    street = set_street_address()
    house_number = set_house_number_address()
    level = None
    apartment_num = None
    while True:
        building = input("Do you live in a building (yes/no)?: ")
        if building == "yes":
            level = set_level_address()
            apartment_num = set_apartment_num_address()
            break
        if building == "no":
            break
    address = Address(city, street, house_number, level, apartment_num)
    customer = Customer(id, first_name, last_name, address, email, birth_day)
    return customer


def book_from_input(library: Library):
    name = set_book_name_for_register()
    print("Book ID should contain all the initials of the book\nand a number at the end that"
          " represent\nthe number of copy of that same book in the library\nfor example: the book"
          " 'Anna Karenina' id will be 'ak1'")
    book_id = set_book_id_for_register(library)
    author = set_book_author_for_register()
    year_published = int(set_year_published_for_register())
    loan_time = set_loan_time_for_register()
    book = Book(book_id, name, author, year_published, loan_time=loan_time)
    return book


def librarian_control_choice():
    possible_answers = ("1", "2", "3", "$")
    while True:
        control_choice = input("1. Library Control\n"
                               "2. Book Control\n"
                               "3. Customer Control\n"
                               "Your choice: ")
        if control_choice not in possible_answers:
            raise InvalidInput("Invalid input, please try again")
        else:
            return control_choice


def librarian_library_control_choice():
    possible_answers = ("1", "2", "3", "4", "$")
    while True:
        library_control_choice = input("1. Display all the current customers\n"
                                       "2. Display all the current books in the library\n"
                                       "3. Display all active loans\n"
                                       "4. Display all late loans\n"
                                       "Your choice: ")
        if library_control_choice not in possible_answers:
            raise InvalidInput("Invalid input, please try again")
        else:
            return library_control_choice


def librarian_book_control_choice():
    possible_answers = ("1", "2", "3", "4", "$")
    while True:
        book_control_choice = input("1. Add new book\n"
                                    "2. Remove a book\n"
                                    "3. Find book by Name\n"
                                    "4. Find book by Author\nYour choice: ")
        if book_control_choice not in possible_answers:
            raise InvalidInput("Invalid input, please try again")
        else:
            return book_control_choice


def librarian_customer_control_choice():
    possible_choices = ("1", "2", "3", "$")
    while True:
        customer_control_choice = input("1. Display all loans for customer\n"
                                        "2. Remove Customer\n"
                                        "3. Find customer by name\n"
                                        "Your choice: ")
        if customer_control_choice not in possible_choices:
            raise InvalidInput("Invalid input, please try again")
        else:
            return customer_control_choice


def customer_choose():
    print("What would you like to do?")
    while True:
        possible_choices = ("1", "2", "$")
        print("1. Loan\n2. Return a book")
        choice = input("choice: ")
        if choice not in possible_choices:
            raise InvalidInput("Invalid Input, please try again")
        else:
            return choice


def check_customer_id(customer_id: str, library: Library):
    library_customer_dict: dict = library.display_customers()
    if customer_id in library_customer_dict.keys():
        return True
    else:
        raise InvalidCustomerID


def check_if_loaned(book_id: str, library: Library):
    if book_id not in library.display_loans().keys():
        raise InvalidLoan
    else:
        return True


def check_loans_for_customer(customer_id: str, library: Library):
    for key, value in library.display_customers().items():
        if key == customer_id:
            customer = value
            if len(customer.display_active_loans()) > 0:
                raise LoanExists
            else:
                return True


def check_late_loans_for_customer(customer_id: str, library: Library):
    late_loans = library.display_late_loans()
    for key, value in late_loans.items():
        loan: Loan = value
        if loan.get_customer_id() == customer_id:
            raise LateLoanExists
    else:
        return True


def back_to_main_menu():
    possible_choice = ("1", "2", "$")
    while True:
        next_step = input("Is there anything else i can help you with?\n1.Yes\n2.No\nChoice: ")
        if next_step not in possible_choice:
            raise InvalidInput("Invalid Input, please try again")
        else:
            return next_step


def display_books_to_customer(library: Library):
    print("The books we currently have are:")
    books = library.display_books()
    count = 1
    for i in books.values():
        print(f"{count} - {i}")
        count += 1


def main_menu():
    print("How can i assist you? \n1. I am a customer\n2. I want to be a customer\n"
          "3. I am a librarian of this library\nIf you want at any point to exit please type: $")
    possible_choices = ("1", "2", "3", "$")
    while True:
        entity = input("choice: ")
        if entity not in possible_choices:
            raise InvalidInput("Invalid input, please try again")
        else:
            return entity
