from datetime import datetime
from entities.person import Person
from helpers import connect as conn
from helpers import checkInteger

class DeleteHistory(Person):
    def __init__(self) -> None:
        self.dhistory = []
        self.address_book_id = "unknown"

    def show_delete_history(self, address_book_id: int) -> None:
        self.address_book_id = address_book_id
        sql = "select * from `delete` where address_book = %s"
        conn.cursor.execute(sql, (self.address_book_id,  ))
        self.dhistory = conn.cursor.fetchall()
        if len(self.dhistory) == 0:
            print("Delete history page is empty")
            return False
        for i in range(len(self.dhistory)):
            info = self.dhistory[i]["Info"].split("-")
            name = info[0].strip()
            surname = info[1].strip()
            numbers = info[2].strip()
            countries = info[3].strip()
            is_blocked = True if info[4].strip() == "True" or info[4].strip() == "1" else False
            address_book_name = info[5].strip()
            print(self.show_person(name, surname, numbers, countries, i + 1, is_blocked, address_book_name))
        return self.dhistory

    def add_delete_history(self, name: str, surname: str, number: str, countries: str, is_blocked: bool, address_book_name: str, address_book_id: int) -> None:
        sql = "insert into `delete` (Info, Date, address_book) values (%s, %s, %s)"
        info = f"{name} - {surname} - {number} - {countries} - {is_blocked} - {address_book_name}"
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.cursor.execute(sql, (info, time, address_book_id))
        conn.connection.commit()

    def delete_delete_history(self, remove: int) -> None:
        if len(self.dhistory) == 0:
            print("There nothing to delete")
            return
        while True:
            if 0 <= int(remove) - 1 < len(self.dhistory):
                del_element =  self.dhistory[int(remove) - 1]["Info"].split("-")
                ans = input("Are you sure? (Y | N): ")
                if ans == "Y" or ans == "y":
                    sql = "DELETE FROM `delete` WHERE Id = %s"
                    conn.cursor.execute(sql, (self.dhistory[int(remove) - 1]["Id"], ))
                    conn.connection.commit()
                    print(f"'{del_element[0].strip()} {del_element[1].strip()}' deleted successfully!")
                break
            else:
                ans = input("Please choose number that is in Delete history page. Do you want to try again? (Y | N): ")
                if ans == "Y" or ans == "y":
                    remove = input("Which one do you want to delete: ")
                    while not checkInteger.is_integer(remove):
                        print("Please enter a number!")
                        remove = input("Which one do you want to delete: ")
                else:
                    break

    def delete_all_delete_history(self) -> None:
        ans = input("Are you sure to delete all delete history! (Y | N): ")
        if ans == "Y" or ans == "y":
            sql = "delete from `delete` where address_book = %s"
            conn.cursor.execute(sql, (self.address_book_id, ))
            conn.connection.commit()
            print("Delete history deleted successfully")
