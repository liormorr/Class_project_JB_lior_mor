import pickle
import re

from backhand.address import Address
from backhand.book import Book
from backhand.customer import Customer
from backhand.library import Library


def set_birthday_for_customer():
    while True:
        birth_day = input("Please insert your birth date (DD-MM-YYYY): ")
        if not re.search('(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[012])-(?:19{2}|20[01][0-9]|2020)', birth_day):
            print("Error, birthday is invalid")
        else:
            return birth_day


def set_email_for_customer():
    while True:
        email = input("Please insert your email: ")
        if not re.search('[a-z0-9]+@[a-z]+\.[a-z]{2,3}', email):
            print("Error, email is invalid")
        else:
            return email


def set_id_for_customer():
    print("ID should contain at least 2 letters and preferably at least 1 number at the end")
    while True:
        id_for_customer = input("Please Enter your desired ID: ")
        if not re.search("^[a-zA-Z]{2,}[0-9_]+$", id_for_customer):
            print("Error, ID should contain only letters and numbers (example: lm1)")
        else:
            return id_for_customer


def set_first_name():
    while True:
        first_name = input("Please enter your first name: ")
        if not first_name.isalpha():
            print("Error, name should contain only letters")
            continue
        if len(first_name) < 2:
            print("Error, name should have more than 1 letter")
            continue
        break
    first_name = first_name.title()
    return first_name


def set_last_name():
    while True:
        last_name = input("Please enter your last name: ")
        if not last_name.isalpha():
            print("Error, name should contain only letters")
            continue
        if len(last_name) < 2:
            print("Error, name should have more than 1 letter")
            continue
        break
    last_name = last_name.title()
    return last_name


def full_name():
    while True:
        first_name = input("Please enter your first name: ")
        if not first_name.isalpha():
            print("Error, name should contain only letters")
            continue
        if len(first_name) < 2:
            print("Error, name should have more than 1 letter")
            continue
        break
    while True:
        last_name = input("Please enter your last name: ")
        if not last_name.isalpha():
            print("Error, last name should contain only letters")
            continue
        if len(last_name) < 2:
            print("Error, last name should have more than 1 letter")
            continue
        break
    name = first_name.title() + " " + last_name.title()
    return name


def set_city_address():
    while True:
        city = input("Please enter the name of your city: ")
        if not re.search("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", city):
            print("Error, city should contain only letters")
            continue
        if len(city) < 2:
            print("Error, city should have more than 1 letter")
            continue
        break
    city = city.title()
    return city


def set_street_address():
    while True:
        street = input("Please enter the name of your street: ")
        if not re.search("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", street):
            print("Error, invalid street input")
            continue
        if len(street) < 2:
            print("Error, street should have more than 1 letter")
            continue
        break
    street = street.title()
    return street


def set_house_number_address():
    while True:
        house_number = input("Please enter the number of your house: ")
        if not house_number.isdigit():
            print("Error, house number should contain only numbers")
            continue
        break
    house_number = int(house_number)
    return house_number


def set_level_address():
    while True:
        level = input("Please enter the number of your level: ")
        if not level.isdigit():
            print("Error, level should contain only numbers")
            continue
        break
    return level


def set_apartment_num_address():
    while True:
        apartment_num = input("Please enter the number of your apartment: ")
        if not apartment_num.isdigit():
            print("Error, apartment number should contain only numbers")
            continue
        break
    return apartment_num


def set_book_name_for_register():
    while True:
        book_name = input("Please enter the Book's name: ")
        if not re.search("[A-Za-z]?", book_name):
            print("Invalid name, please try again")
            continue
        else:
            return book_name


def set_book_id_for_register():
    while True:
        book_id = input("Please type the book ID: ")
        if not re.search("^[a-zA-Z]{2,}[0-9]*$", book_id):
            print("Invalid ID, please try again")
            continue
        else:
            return book_id


def set_book_author_for_register():
    while True:
        book_author = input("Please type the book publisher name: ")
        if not re.search("^[a-zA-Z\s]+$", book_author):
            print("Invalid publisher name, please try again")
            continue
        else:
            return book_author


def set_year_published_for_register():
    while True:
        year_published = input("Please enter the year the book published: ")
        if not re.search("^[12][0-9]{3}$", year_published):
            print("Invalid year entered, please try again")
            continue
        else:
            return year_published


def set_loan_time_for_register():
    while True:
        loan_time_options = ("1", "2", "3")
        loan_time_typed = input("'1' means up 10 days\n'2' means up to 5 days\n'3' means up to 2 days\n"
                                "Please enter the loan time for the book: ")
        if loan_time_typed not in loan_time_options:
            print("Invalid input")
            continue
        else:
            loan_time_typed = int(loan_time_typed)
            return loan_time_typed


def customer_from_input():
    first_name = set_first_name()
    last_name = set_last_name()
    id = set_id_for_customer()
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


def book_from_input():
    name = set_book_name_for_register()
    print("Book ID should contain all the initials of the book\nand a number at the end that"
          "represent\nthe number of copy of that same book in the library\nfor example: the book"
          " 'Anna Karenina' id will be 'ak1'")
    book_id = set_book_id_for_register()
    author = set_book_author_for_register()
    year_published = int(set_year_published_for_register())
    loan_time = set_loan_time_for_register()
    book = Book(book_id, name, author, year_published, loan_time=loan_time)
    return book


def librarian_choose():
    librarian_choice = input("1. Add a new book to the Library? \n2. Display all the current customers? \n"
                             "3. Display all the current books in the library? \n4. Remove a book from our "
                             "shelf? \n5. Display all active loans?\n"
                             "6. Display all late loans\nYour choice: ")
    return librarian_choice


def customer_choose():
    print("What would you like to do?")
    while True:
        possible_choices = ("1", "2", "$")
        print("1. Loan\n2. Return a book")
        choice = input("choice: ")
        if choice not in possible_choices:
            print("Invalid Input, please try again")
            continue
        else:
            return choice


def check_customer_id(customer_id: str, library: Library):
    library_customer_dict: dict = library.display_customers()
    if customer_id in library_customer_dict.keys():
        return False
    else:
        return True


def back_to_main_menu():
    possible_choice = ("1", "2", "$")
    while True:
        next_step = input("Is there anything else i can help you with?\n1.Yes\n2.No\nChoice: ")
        if next_step not in possible_choice:
            print("Invalid Input, please try again")
            continue
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
    entity = input("choice: ")
    possible_choices = ("1", "2", "3", "$")
    while True:
        if entity not in possible_choices:
            print("Invalid input, please try again")
            continue
        else:
            break
    return entity
