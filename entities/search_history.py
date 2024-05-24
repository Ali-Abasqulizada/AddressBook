from datetime import datetime
from helpers import connect as conn
from helpers import checkInteger
class SeachHistory:
    def __init__(self) -> None:
        self.shistory = []

    def show_search_history(self, address_book_id: int) -> None:
        sql = "select * from search where address_book = %s"
        conn.cursor.execute(sql, (address_book_id, ))
        self.shistory = conn.cursor.fetchall()
        if len(self.shistory) == 0:
            print("Search history page is empty")
            return False
        for i in range(len(self.shistory)):
            print(f"{i + 1} ---> {self.shistory[i]["Info"]}")
        return True
    
    def add_search_history(self, name: str, address_book_name: str, address_book_id: int) -> None:
        sql = "insert into search (Info, address_book) values (%s, %s)"
        info = f"'{name}' is searched in '{address_book_name}' address book at {datetime.now().strftime('%d-%m-%Y- %H:%M')}"
        conn.cursor.execute(sql, (info, address_book_id))
        conn.connection.commit()

    def delete_search_history(self, remove: int, address_book_name: str) -> None:
        if len(self.shistory) == 0:
            print("There nothing to delete")
            return
        while True:
            if 0 <= int(remove) - 1 < len(self.shistory):
                del_element =  [self.shistory[int(remove) - 1]["Info"], self.shistory[int(remove) - 1]["address_book"]]
                ans = input("Are you sure? (Y | N): ")
                if ans == "Y" or ans == "y":
                    sql = "DELETE FROM search WHERE Info = %s and address_book = %s"
                    conn.cursor.execute(sql, (del_element[0], del_element[1]))
                    conn.connection.commit()
                    print(f"'{del_element[0]}' successfully deleted from '{address_book_name}' address book!")
                break
            else:
                ans = input("Please choose number that is in Search history page. Do you want to try again? (Y | N): ")
                if ans == "Y" or ans == "y":
                    remove = input("Which one do you want to delete: ")
                    while not checkInteger.is_integer(remove):
                        print("Please enter a number!")
                        remove = input("Which one do you want to delete: ")
                else:
                    break

    def delete_all_search_history(self, address_book_name: str, address_book_id: int) -> None:
        ans = input(f"Are you sure to delete all search history from {address_book_name} address book! (Y | N): ")
        if ans == "Y" or ans == "y":
            sql = "DELETE FROM search WHERE address_book = %s"
            conn.cursor.execute(sql, (address_book_id, ))
            conn.connection.commit()
            print(f"Search history in {address_book_name} address book deleted successfully")