import os
import pickle
from datetime import datetime

from backhand.address import Address
from backhand.book import Book
from backhand.customer import Customer
from backhand.inputs import *
from backhand.library import Library

if __name__ == '__main__':
    library_file = None
    if os.path.exists('./library_files/library.pickle'):
        with open('./library_files/library.pickle', 'rb') as f:
            library_file = pickle.load(f)
    else:
        my_lib_address = Address("Kfar Yona", "Ahavat Adam", 79)
        my_lib = Library("Saint Lior's Regional Community Library", my_lib_address)
        anna_karenina = Book("ak1", "Anna Karenina", "Leo Tolstoy", 1878)
        to_kill_a_mockingbird = Book("tkam1", "To Kill a MockingBird", "Harper Lee", 1960)
        the_great_gatsby = Book("tgg1", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        my_lib.add_new_book(anna_karenina)
        my_lib.add_new_book(to_kill_a_mockingbird)
        my_lib.add_new_book(the_great_gatsby)
        my_lib.add_new_book(anna_karenina)
        lior_mor_address = Address("Kfar Yona", "Ahavat Adam", 79)
        lior_mor = Customer("lm1", "Lior", "Mor", lior_mor_address, "liormorr@gmail.com", "4.9.90")
        my_lib.add_new_customer(lior_mor)

    print(f"Hello and welcome to '{my_lib.get_name()}'")

    try:
        while True:
            entity = main_menu()  # 1.Customer 2.New customer 3.Librarian
            if entity == "$":
                print("May your journey be long and fulfilling")
                exit(0)
            while entity == "1":  # Customer
                customer = None
                customer_id = None
                customer_choice = customer_choose()
                if customer_choice == "$":
                    print("Thank you for stopping by, have a great day!")
                    exit(0)
                if customer_choice == "1":  # Loan a Book
                    while customer_id is None:
                        customer_id = input("What is your Customer ID?: ")
                        if check_customer_id(customer_id, my_lib):
                            print("Id already in our system, please try again")
                            continue
                        customers = my_lib.display_customers()
                        for key, value in customers.items():
                            if customer_id == key:
                                customer = value
                        print(f"Hello {customer.get_name()}, what would you like to do?")
                        break
                    display_books_to_customer(my_lib)
                    books = my_lib.display_books()
                    while True:
                        book_id = input("What is your choice (by Book ID)?: ")
                        if book_id not in books.keys():
                            print("Invalid Key, please Try again")
                            continue
                        for key, value in books.items():
                            if key == book_id:
                                print(f"You chose the book: {value}")
                                confirm_book = input("Correct?:\n1. Yes\n2. No\nYour Choice: ")
                                book = value
                                if confirm_book == "1":  # Yes
                                    my_lib.loan_book(value, key, customer)
                                    time = datetime.strftime((datetime.now() + book.get_loan_time_duration()),
                                                             "%d/%m/%Y")
                                    print(f"Great Success the Book {book} is yours until - {time}")
                                    print("-------------------------------------------------------")
                                    break
                                elif confirm_book == "2":  # No
                                    break
                        next_step = back_to_main_menu()
                        if next_step == "1":
                            print("Going back to Main Menu")
                            print("----------------------------")
                            break
                        elif next_step == "2" or next_step == "$":
                            print("Have a great day now, bye bye")
                            exit(0)
                if customer_choice == "2":  # Return a Book
                    while True:
                        count = 0
                        return_book_id = input("What is the Book ID: ")
                        if return_book_id not in my_lib.display_loans().keys():
                            print("This book is not loaned, or you entered invalid Book ID, try again")
                            count += 1
                            continue
                        print(f"The book you want to return is {my_lib.display_loans[return_book_id]}")
                        return_to_main = back_to_main_menu()
                    break
            while entity == "2":
                print("Glad you are.")
                customer = customer_from_input()
                my_lib.add_new_customer(customer)
                print(f"Great, you are now a customer at '{my_lib.get_name()}'")
                next_step = back_to_main_menu()
                if next_step == "1":
                    print("Going back to Main Menu")
                    print("----------------------------")
                    break
                elif next_step == "2" or next_step == "$":
                    print("Have a great day now, bye bye")
                    exit(0)

            while entity == "3":
                print("What would you like to do?")
                librarian_choice = librarian_choose()
                if librarian_choice == "$":
                    print("Logging out...")
                    exit(0)
                if librarian_choice == "1":
                    book = book_from_input()
                    if my_lib.add_new_book(book):
                        print(f"Done, the book {book.get_name()} successfully added to the library")
                    next_step = back_to_main_menu()
                    if next_step == "$" or next_step == "2":
                        print("Off with ya")
                        exit(0)
                    elif next_step == "1":
                        print("Going back to Main Menu")
                        print("----------------------------")
                        break
                if librarian_choice == "2":
                    for key, value in my_lib.display_customers().items():
                        print(f"{value}\n")
                if librarian_choice == "3":
                    for key, value in my_lib.display_books().items():
                        print(f"{value}\n")
                if librarian_choice == "4":
                    books_list = my_lib.display_books()
                    for key, value in books_list.items():
                        print(value)
                    choice = input("Choose a book by ID: ")
                    for key, value in books_list.items():
                        if choice == key:
                            book_id = key
                            while not my_lib.remove_book(book_id):
                                print("Invalid key, try again")
                                continue
                            else:
                                print(f"Great! the book {value} removed from the library")
                                break
                next_step = back_to_main_menu()
                if next_step == "$" or next_step == "2":
                    print("Off with ya")
                    exit(0)
                elif next_step == "1":
                    print("Going back to Main Menu")
                    print("----------------------------")
                    break

    finally:
        pass
        # with open('library.pickle', 'wb') as f:
        #     pickle.dump(my_lib, f)
