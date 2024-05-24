class Operations:
    def __init__(self) -> None:
        pass

    def address_operations(self) -> None:
        print('''
    Choose an operation please --->
        Operations:
            1 -> Show all Address Books
            2 -> Delete all Address Books
            3 -> Add new Address Book
            4 -> Delete an Address Book
            5 -> Enter in an Address Book
            show -> Show operations
            exit -> Exit
    ''')

    def main_operations(self) -> None:
        print('''
    Choose an Address book operation please --->
        Operations:
            1 -> Show all people on Address Book
            2 -> Delete all people from Address Book
            3 -> Add a person to Address Book
            4 -> Search someone
            5 -> Edit
            6 -> Show search history
            7 -> Show deleted people
            8 -> Show blocked people
            9 -> Show edit history
            back -> go back
            show -> Show operations
    ''')
    
    def edit_operations(self) -> None:
        print('''
    Which operation do you want to continue?
        Operations:
            1 -> Edit name
            2 -> Edit Surname
            3 -> Edit Number|s
            4 -> Delete
            5 -> Block | Unblock
            back -> go back
            show -> Show edit operations
            ''')
    
    def search_operations(self) -> None:
        print('''
    Which operation do you want to continue?
        Operations:
            1 -> Delete all search history
            2 -> Delete a search history
            back -> go back
            show -> Show search operations
            ''')
        
    def delete_operations(self) -> None:
        print('''
    Which operation do you want to continue?
        Operations:
            1 -> Delete all delete history
            2 -> Delete a delete history
            3 -> Add deleted person back to Address Book
            back -> go back
            show -> Show delete operations
            ''')
        
    def edit_history_operations(self) -> None:
        print('''
    Which operation do you want to continue?
        Operations:
            1 -> Delete all edit history
            2 -> Delete a edit history
            back -> go back
            show -> Show edit history operations
            ''')