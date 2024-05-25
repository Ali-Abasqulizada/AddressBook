from entities.delete_history import DeleteHistory
from helpers import checkInteger
from helpers import connect as conn
class Delete(DeleteHistory):
    def __init__(self) -> None:
        self.people = []
        self.id = 0

    def delete_person(self, people: list, id: int, address_book_name: str, address_book_id: int) -> None:
        self.people = people
        self.id = id
        if len(self.people) == 1:
            self.id = 0
        ans = input(f"Are you sure to delete '{self.people[self.id]["Name"]} {self.people[self.id]["Surname"]}' in '{address_book_name}' address book? (Y | N): ")
        if ans == "Y" or ans == "y":
            sql = f"delete from people where Id = {self.people[self.id]["Id"]}"
            sql2 = "update address set Total = Total - 1 where Id = %s"
            conn.cursor.execute(sql)
            conn.cursor.execute(sql2, (address_book_id, ))
            conn.connection.commit()
            print(f"{self.people[self.id]["Name"]} {self.people[self.id]["Surname"]} is deleted successfully")
            return True
        return False


    def add_back(self, address_book_name: str, address_book_id: int) -> None:
        sql = "select * from `delete` where address_book = %s"
        conn.cursor.execute(sql, (address_book_id, ))
        deletedPeople = conn.cursor.fetchall()
        ans = 1
        if len(deletedPeople) > 1:
            ans = input("Which one do want add back. Please enter id: ")
            while not checkInteger.is_integer(ans) or int(ans) <= 0 or int(ans) > len(deletedPeople):
                ans = input("Please enter valid id: ")
        info = deletedPeople[int(ans) - 1]["Info"].split("-")
        name = info[0].strip()
        surname = info[1].strip()
        numbers = info[2].strip()
        countries = info[3].strip()
        is_blocked = 1 if info[4].strip() == "True" or info[4].strip() == "1" else 0
        try:
            sql1 = "insert into People (Name, Surname, Number, Country, Is_blocked, address_book) values(%s, %s, %s, %s, %s, %s)"
            sql2 = f"delete from `delete` where Id = {deletedPeople[int(ans) - 1]["Id"]}"
            sql3 = "update address set Total = Total + 1 where Id = %s"
            conn.cursor.execute(sql1, (name, surname, numbers, countries, is_blocked, address_book_id))
            conn.cursor.execute(sql2)
            conn.cursor.execute(sql3, (address_book_id, ))
            conn.connection.commit()
            print(f"'{name} {surname}' is successfully added back to '{address_book_name}' address book")
        except:
            print(f"'{name} {surname}' is already exists in '{address_book_name}' address book")