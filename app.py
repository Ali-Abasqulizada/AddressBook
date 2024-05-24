from entities.address import Address
from entities.person import Person
from entities.search import Search
from entities.edit import Edit
from helpers import checkInteger
from helpers.operation import Operations
AD = Address()
OP = Operations()
PER = Person()
SER = Search()
ED = Edit()
print("WELCOME TO ADDRESS BOOK")
OP.address_operations()
if __name__ == "__main__":
    while True:
        main_ans = input("Please enter an operation: ")
        if main_ans == "1":
            AD.show_all_address()
        elif main_ans == "2":
            AD.delete_all_address()
        elif main_ans == "3":
            name = input("Please enter name of new Address Book: ")
            AD.create_new_address(name)
        elif main_ans == "4":
            AD.delete_address()
        elif main_ans == "5":
            address_book_name, address_book_id = AD.enter_address()
            if address_book_id:
                OP.main_operations()
                while True:
                    ans = input("Please enter address book an operation: ")
                    if ans == "1":
                        PER.show_all_people(address_book_name, address_book_id)
                    elif ans == "2":
                        PER.delete_all_people(address_book_name, address_book_id)
                    elif ans == "3":
                        name = input("Please enter a name: ")
                        surname = input("Please enter a surname: ")
                        number = input("Please enter a number: ")
                        PER.add_person(name, surname, number, address_book_name, address_book_id)
                    elif ans == "4":
                        name = input("Please enter the name that do you want to search: ")
                        SER.search(name, address_book_name, address_book_id)
                    elif ans == "5":
                        name = input("Please enter the name that do you want to edit: ")
                        check = ED.edit(name, address_book_name, address_book_id)
                        if check:
                            OP.edit_operations()
                            while True:
                                ans2 = input("Please enter a edit operation: ")
                                if ans2 == "1":
                                    changeName = input("Please enter new name: ")
                                    ED.edit_name(changeName)
                                elif ans2 == "2":
                                    changeSurname = input("Please enter new surname: ")
                                    ED.edit_surname(changeSurname)
                                elif ans2 == "3":
                                    changeNumber = input("Please enter new number: ")
                                    ED.edit_number(changeNumber)
                                elif ans2 == "4":
                                    ED.delete_person_edit()
                                    break
                                elif ans2 == "5":
                                    ED.block_person_edit()
                                    break
                                elif ans2.lower() == "back":
                                    print("Going back from Edit page")
                                    break
                                elif ans2.lower() == "show":
                                    OP.edit_operations()
                                else:
                                    print("Invalid edit operation")
                    elif ans == "6":
                        check = SER.show_search_history(address_book_id)
                        if check:
                            OP.search_operations()
                            while True:
                                ans2 = input("Please enter a search history operation: ")
                                if ans2 == "1":
                                    SER.delete_all_search_history(address_book_name, address_book_id)
                                    break
                                elif ans2 == "2":
                                    remove = input("Which one do you want to delete: ")
                                    while not checkInteger.is_integer(remove):
                                        print("Please enter a number!")
                                        remove = input("Which one do you want to delete: ")
                                    SER.delete_search_history(int(remove), address_book_name)
                                    break
                                elif ans2.lower() == "back":
                                    print("Going back from Search history page")
                                    break
                                elif ans2.lower() == "show":
                                    OP.search_operations()
                                else:
                                    print("Invalid search history operation")
                    elif ans == "7":
                        check = ED.show_delete_history(address_book_id)
                        if check:
                            OP.delete_operations()
                            while True:
                                ans2 = input("Please enter a delete history operation: ")
                                if ans2 == "1":
                                    ED.delete_all_delete_history()
                                    break
                                elif ans2 == "2":
                                    remove = input("Which one do you want to delete: ")
                                    while not checkInteger.is_integer(remove):
                                        print("Please enter a number!")
                                        remove = input("Which one do you want to delete: ")
                                    ED.delete_delete_history(int(remove))
                                    break
                                elif ans2 == "3":
                                    ED.add_back(address_book_name, address_book_id)
                                    break
                                elif ans2.lower() == "back":
                                    print("Going back from Delete history page")
                                    break
                                elif ans2.lower() == "show":
                                    OP.delete_operations()
                                else:
                                    print("Invalid Delete history operation")
                    elif ans == "8":
                        ED.show_block_history_edit(address_book_name, address_book_id)
                    elif ans == "9":
                        check = ED.show_edit_history(address_book_id)
                        if check:
                            OP.edit_history_operations()
                            while True:
                                ans2 = input("Please enter a edit history operation: ")
                                if ans2 == "1":
                                    ED.delete_all_edit_history()
                                    break
                                elif ans2 == "2":
                                    remove = input("Which one do you want to delete: ")
                                    while not checkInteger.is_integer(remove):
                                        print("Please enter a number!")
                                        remove = input("Which one do you want to delete: ")
                                    ED.delete_edit_history(int(remove))
                                    break
                                elif ans2.lower() == "back":
                                    print("Going back from Edit history page")
                                    break
                                elif ans2.lower() == "show":
                                    OP.edit_history_operations()
                                else:
                                    print("Invalid edit history operation")
                    elif ans.lower() == "back":
                        print("Going back from Address Book page")
                        break
                    elif ans.lower() == "show":
                        OP.main_operations()
                    else:
                        print("Invalid operation!")
        elif main_ans.lower() == "show":
            OP.address_operations()
        elif main_ans.lower() == "exit":
            print("GOODBYE :) ")
            break
        else:
            print("Invalid operation!")