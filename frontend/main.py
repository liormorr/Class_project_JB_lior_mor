import os
import time
from datetime import datetime
from backend.inputs import *
from backend.library import Library

if __name__ == '__main__':
    library_file = None
    if os.path.exists('library.pickle'):
        with open('library.pickle', 'rb') as f:
            library_file = pickle.load(f)

    else:
        my_lib_address = Address("Kfar Yona", "Ahavat Adam", 79)
        library_file = Library("Saint Lior's Regional Community Library", my_lib_address)
        anna_karenina = Book("ak1", "Anna Karenina", "Leo Tolstoy", 1878)
        to_kill_a_mockingbird = Book("tkam1", "To Kill a MockingBird", "Harper Lee", 1960)
        the_great_gatsby = Book("tgg1", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library_file.add_new_book(anna_karenina)
        library_file.add_new_book(to_kill_a_mockingbird)
        library_file.add_new_book(the_great_gatsby)
        library_file.add_new_book(anna_karenina)
        lior_mor_address = Address("Kfar Yona", "Ahavat Adam", 79)
        lior_mor = Customer("lm1", "Lior", "Mor", lior_mor_address, "liormorr@gmail.com", "4.9.90")
        library_file.add_new_customer(lior_mor)

    print(f"Hello and welcome to '{library_file.get_name()}'")
    library_file.check_late_loans()
    try:
        library_file.check_late_loans()
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
                    while customer is None:
                        try:
                            customer_id = input("What is your Customer ID?: ")
                            check_customer_id(customer_id, library_file)
                        except InvalidCustomerID:
                            print("Customer ID does not exists, or typed wrong.")
                            continue
                        customers = library_file.display_customers()
                        for key, value in customers.items():
                            if customer_id == key:
                                customer = value
                                break
                    print(f"Hello {customer.get_name()}, what would you like to do?")
                    try:
                        check_late_loans_for_customer(customer_id, library_file)
                    except LateLoanExists:
                        print("Seems that you have a loan that past its due date, you cannot loan another"
                              " book at this moment")
                        print("--- Returning to Main Menu ---")
                        break
                    display_books_to_customer(library_file)
                    books = library_file.display_books()
                    while True:
                        try:
                            book_id = input("What is your choice (by Book ID)?: ")
                            check_book_id(book_id, library_file)
                        except InvalidBookID:
                            print("The book id you entered is invalid")
                            continue
                        else:
                            for key, value in books.items():
                                if key == book_id:
                                    print(f"You chose the book: {value}")
                                    try:
                                        confirm_book = input("Correct?:\n1. Yes\n2. No\nYour Choice: ")
                                        choice_confirmation(confirm_book)
                                    except InvalidInput:
                                        print("The book id you entered is invalid")
                                        continue
                                    book = value
                                    if confirm_book == "1":  # Yes
                                        library_file.loan_book(value, key, customer)
                                        time = datetime.strftime((datetime.now() + book.get_loan_time_duration()),
                                                                 "%d/%m/%Y")
                                        print(f"Great Success the Book {book} is yours until - {time}")
                                        print("-------------------------------------------------------")
                                        break
                                    elif confirm_book == "2":  # No
                                        break
                        try:
                            next_step = back_to_main_menu()
                        except InvalidInput:
                            print("Invalid Input")
                        else:
                            if next_step == "1":
                                print("Going back to Main Menu")
                                print("----------------------------")
                                entity = None
                                break
                            elif next_step == "2" or next_step == "$":
                                print("Have a great day now, bye bye")
                                exit(0)
                            break
                        break
                if customer_choice == "2":  # Return a Book
                    while customer is None:
                        try:
                            customer_id = input("What is your Customer ID?: ")
                            check_customer_id(customer_id, library_file)
                        except InvalidCustomerID:
                            print("Customer ID does not exists, or typed wrong.")
                            continue
                        customers = library_file.display_customers()
                        for key, value in customers.items():
                            if customer_id == key:
                                customer = value
                        print(f"Hello {customer.get_name()}, what would you like to do?")
                        break
                    if len(customer.display_active_loans()) == 0:
                        print("You dont have active loans")
                        print("--- Going back to Main Menu ---")
                        time.sleep(2)
                        break
                    else:
                        print(customer.display_active_loans())
                    while True:
                        try:
                            return_book_id = input("What is the Book ID: ")
                            check_if_loaned(return_book_id, library_file)
                        except InvalidLoan:
                            print("This book is not loaned, or you entered invalid Book ID, try again")
                            continue
                        else:
                            for key, value in library_file.display_loans().items():
                                if key == return_book_id:
                                    library_file.return_book(value, key, customer)
                                    print(f"The book: {value} safely returned")
                    while True:
                        try:
                            next_step = back_to_main_menu()
                        except InvalidInput:
                            print("Invalid Input")
                            continue
                        else:
                            if next_step == "1":
                                print("Going back to Main Menu")
                                print("----------------------------")
                                entity = None
                                break
                            elif next_step == "2" or next_step == "$":
                                print("Have a great day now, bye bye")
                                exit(0)
                        break
            while entity == "2":  # New Customer
                print("Glad you are.")
                while True:
                    try:
                        customer = customer_from_input(library_file)
                    except InvalidInput:
                        print("Invalid Input")
                        continue
                    except CustomerIDError:
                        print("Error, ID should contain only letters and numbers (example: lm1)")
                        continue
                    except CustomerIDExists:
                        print("Customer ID already exists in our system, try somthing else")
                        continue
                    except EmailError:
                        print("Error, email is invalid")
                        continue
                    except BirthDayError:
                        print("Error, birthday is invalid")
                        continue
                    except AddressError:
                        print("Error, somthing is wrong with your address")
                        continue
                    else:
                        break
                library_file.add_new_customer(customer)
                print(f"Great, you are now a customer at '{library_file.get_name()}'")
                while True:
                    try:
                        next_step = back_to_main_menu()
                    except InvalidInput:
                        print("Invalid Input")
                        continue
                    else:
                        if next_step == "1":
                            print("Going back to Main Menu")
                            print("----------------------------")
                            entity = None
                            break
                        elif next_step == "2" or next_step == "$":
                            print("Have a great day now, bye bye")
                            exit(0)
                    break
            while entity == "3":  # Librarian
                print("What would you like to do?")
                while True:
                    try:
                        librarian_control_choose = librarian_control_choice()
                    except InvalidInput:
                        print("Invalid Input")
                        continue
                    else:
                        break
                if librarian_control_choose == "$":  # Exit
                    print("Logging out...")
                    exit(0)
                if librarian_control_choose == "1":  # Library Control
                    print("---- Library Control Panel ----")
                    while True:
                        try:
                            librarian_library_control = librarian_library_control_choice()
                        except InvalidInput:
                            print("Invalid Input")
                            continue
                        else:
                            break
                    if librarian_library_control == "$":  # Exit
                        print("Logging out...")
                        exit(0)
                    if librarian_library_control == "1":  # Display Customers
                        for key, value in library_file.display_customers().items():
                            print(f"{value}\n")
                    if librarian_library_control == "2":  # Display Books
                        for key, value in library_file.display_books().items():
                            print(f"- {value}")
                        print("-------------------")
                    if librarian_library_control == "3":  # Display Active Loans
                        loan_dict = library_file.display_loans()
                        if len(loan_dict) == 0:
                            print("There are no active loans at this moment")
                        else:
                            for key, value in loan_dict.items():
                                print(value)
                        print("-------------------")
                    if librarian_library_control == "4":  # Display Late Loans
                        late_loan_dict = library_file.display_late_loans()
                        if len(late_loan_dict) == 0:
                            print("There are no active late loans at this moment")
                        else:
                            for key, value in late_loan_dict.items():
                                print(value)
                            print("-------------------")
                if librarian_control_choose == "2":  # Book Control
                    print("---- Book Control Panel ----")
                    while True:
                        try:
                            librarian_book_control = librarian_book_control_choice()
                        except InvalidInput:
                            print("Invalid Input")
                            continue
                        else:
                            break
                    if librarian_book_control == "$":  # Exit
                        print("Logging out...")
                        exit(0)
                    if librarian_book_control == "1":  # Add new book
                        while True:
                            try:
                                book = book_from_input()
                            except BookInsertionError:
                                print("Error in book details.")
                                continue
                            else:
                                break
                        if library_file.add_new_book(book):
                            print(f"Done, the book {book.get_name()} "
                                  f"successfully added to the library")
                    if librarian_book_control == "2":  # Remove book
                        books_list = library_file.display_books()
                        for key, value in books_list.items():
                            print(f"- {value}")
                        while True:
                            try:
                                book_id = input("What is your choice (by Book ID)?: ")
                                check_book_id(book_id, library_file)
                            except InvalidBookID:
                                print("The book id you entered is invalid")
                                continue
                            else:
                                for key, value in books_list.items():
                                    if key == book_id:
                                        print(f"Great! the book {value} removed from the library")
                                        library_file.remove_book(book_id)
                                        break
                            break
                    if librarian_book_control == "3":  # Search book by name
                        book_name = input("Please type the name of the book you want to search for: ").title()
                        books_list = library_file.display_books()
                        count = 1
                        books_in_library = len(books_list)
                        for key, value in books_list.items():
                            book: Book = value
                            if count == books_in_library:
                                print("--- Book Not found ---")
                                time.sleep(2)
                                break
                            if book.get_name() == book_name:
                                print(book)
                                break
                            if book.get_name() != book_name:
                                count += 1
                                continue
                    if librarian_book_control == "4":  # Search book by author
                        book_author = input("Please type the name of the book you want to search for: ").title()
                        books_list = library_file.display_books()
                        for key, value in books_list.items():
                            book: Book = value
                            if book.get_author() == book_author:
                                print(book)
                                break
                if librarian_control_choose == "3":  # Customer control
                    print("---- Customer Control Panel ----")
                    while True:
                        try:
                            librarian_customer_control = librarian_customer_control_choice()
                        except InvalidInput:
                            print("Invalid Input")
                            continue
                        else:
                            break
                    if librarian_customer_control == "1":  # Display loans for customer
                        while True:
                            try:
                                customer_id = input("What is your Customer ID?: ")
                                check_customer_id(customer_id, library_file)
                            except InvalidCustomerID:
                                print("ID not in our system, please try again")
                                continue
                            else:
                                break
                        customers = library_file.display_customers()
                        customer: Customer = None
                        for key, value in customers.items():
                            if customer_id == key:
                                customer = value
                                break
                        customer_loans = customer.display_active_loans()
                        if len(customer_loans) == 0:
                            print("There are no active loans for that customer")
                        else:
                            customer_name = customer.get_name()
                            print(f"The Customer {customer_name} active loans are: ")
                            for key, value in customer_loans.items():
                                print(value)
                    if librarian_customer_control == "2":  # Remove customer
                        while True:
                            try:
                                customer_id = input("What is your Customer ID?: ")
                                check_customer_id(customer_id, library_file)
                            except InvalidCustomerID:
                                print("ID not in our system, please try again")
                                continue
                            else:
                                break
                        customer = library_file.get_customer(customer_id)
                        if library_file.remove_customer(customer):
                            print(f"The customer {customer.get_name()} has been removed from the library")
                    if librarian_customer_control == "3":  # Find customer by name
                        customer_name = input("Please enter desired customer name: ").title()
                        customer_list = library_file.display_customers()
                        count = 1
                        customers_num = len(customer_list)
                        for key, value in customer_list.items():
                            customer: Customer = value
                            if count == customers_num:
                                print(f"Customer: '{customer_name}' not Found.")
                                break
                            if customer.get_name() != customer_name:
                                count += 1
                                continue
                            if customer.get_name() == customer_name:
                                print(value)
                                break
                while True:
                    try:
                        next_step = back_to_main_menu()
                    except InvalidInput:
                        print("Invalid Input")
                        continue
                    else:
                        if next_step == "1":
                            print("Going back to Main Menu")
                            print("----------------------------")
                            entity = None
                            break
                        elif next_step == "2" or next_step == "$":
                            print("Have a great day now, bye bye")
                            exit(0)
                    break

    except Exception:
        print("Something went wrong")
    finally:
        pass

        # with open('library.pickle', 'wb') as f:
        #     pickle.dump(library_file, f)
