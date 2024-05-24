from datetime import datetime
from helpers import connect as conn
from helpers import checkInteger
class EditHistory:
    def __init__(self) -> None:
        self.ehistory = []
        self.address_book_id = "unknown"
    def show_edit_history(self, address_book_id) -> None:
        self.address_book_id = address_book_id
        sql = "select * from edit where address_book = %s"
        conn.cursor.execute(sql, (self.address_book_id, ))
        self.ehistory = conn.cursor.fetchall()
        if len(self.ehistory) == 0:
            print("Edit history page is empty")
            return False
        for i in range(len(self.ehistory)):
            print(f"{i + 1} ---> {self.ehistory[i]["Info"]}")
        return True

    def add_edit_history(self, old: str, new: str, address_book_name: str, address_book_id: int) -> None:
        sql = "insert into edit (Info, address_book) values (%s, %s)"
        info = f"'{old}' is changed to '{new}' in '{address_book_name}' address book at {datetime.now().strftime('%d-%m-%Y- %H:%M')}"
        conn.cursor.execute(sql, (info, address_book_id))
        conn.connection.commit()

    def delete_edit_history(self, remove: int) -> None:
        if len(self.ehistory) == 0:
            print("There nothing to delete")
            return
        while True:
            if 0 <= int(remove) - 1 < len(self.ehistory):
                del_element =  self.ehistory[int(remove) - 1]["Info"]
                ans = input("Are you sure? (Y | N): ")
                if ans == "Y" or ans == "y":
                    sql = "DELETE FROM edit WHERE Info = %s"
                    conn.cursor.execute(sql, (del_element, ))
                    conn.connection.commit()
                    print(f"'{del_element}' deleted successfully!")
                break
            else:
                ans = input("Please choose number that is in Edit history page. Do you want to try again? (Y | N): ")
                if ans == "Y" or ans == "y":
                    remove = input("Which one do you want to delete: ")
                    while not checkInteger.is_integer(remove):
                        print("Please enter a number!")
                        remove = input("Which one do you want to delete: ")
                else:
                    break

    def delete_all_edit_history(self) -> None:
        ans = input("Are you sure to delete all edit history! (Y | N): ")
        if ans == "Y" or ans == "y":
            sql = "Delete from edit where address_book = %s"
            conn.cursor.execute(sql, (self.address_book_id, ))
            conn.connection.commit()
            print("Edit history deleted successfully")