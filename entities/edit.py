from entities.search import Search
from helpers import checkInteger
from helpers import connect as conn
from entities.edit_history import EditHistory
from entities.delete import Delete
from entities.block import Block
class Edit(Search, EditHistory, Delete, Block):
    def __init__(self) -> None:
        self.people = []
        self.id = 0
        self.address_book_name = "unknown"
        self.address_book_id = "unknown"

    def edit(self, name: str, address_book_name: str, address_book_id: int) -> bool:
        self.address_book_name = address_book_name
        self.address_book_id = address_book_id
        self.people, newName = self.search(name, self.address_book_name, self.address_book_id)
        if len(self.people) == 0:
            return False
        elif len(self.people) > 1:
            ans = input(f"There multiple people that its name starts with '{newName}'. Please choose id of person that do you want to edit: ")
            while not checkInteger.is_integer(ans) or int(ans) <= 0 or int(ans) > len(self.people):
                ans = input("Please enter valid id: ")
            self.id = int(ans) - 1
            print(self.show_person(self.people[self.id]["Name"], self.people[self.id]["Surname"], self.people[self.id]["Number"], self.people[self.id]["Country"], self.id + 1, self.people[self.id]["Is_blocked"], self.address_book_name))
        return True
    
    def edit_name(self, name: str) -> None:
        sql = "update people set Name = %s where Id = %s"
        ans = input(f"Are you sure to change '{self.people[self.id]["Name"]}' name to '{name}' (Y | N): ")
        if ans == "Y" or ans == "y":
            conn.cursor.execute(sql, (name, self.people[self.id]["Id"]))
            conn.connection.commit()
            print(f"'{self.people[self.id]["Name"]}' name succesfully changed to '{name}'")
            self.add_edit_history(self.people[self.id]["Name"], name, self.address_book_name, self.address_book_id)
            self.people[self.id]["Name"] = name

    def edit_surname(self, surname: str) -> None:
        sql = "update people set Surname = %s where Id = %s"
        ans = input(f"Are you sure to change '{self.people[self.id]["Surname"]}' name to '{surname}' (Y | N): ")
        if ans == "Y" or ans == "y":
            conn.cursor.execute(sql, (surname, self.people[self.id]["Id"]))
            conn.connection.commit()
            print(f"'{self.people[self.id]["Surname"]}' surname succesfully changed to '{surname}'")
            self.add_edit_history(self.people[self.id]["Surname"], surname, self.address_book_name, self.address_book_id)
            self.people[self.id]["Surname"] = surname

    def edit_number(self, number: str) -> None:
        while not self.check_number(number):
            number = input("please enter number: ")
        country = self.check_country(number)
        numbers = self.people[self.id]["Number"].split(",")
        countries = self.people[self.id]["Country"].split(",")
        ans = 1
        if len(numbers) > 1:
            for n in range(len(numbers)):
                print(f"{n + 1} -> {numbers[n]}")
            ans = input(f"'{self.people[self.id]["Name"]}' has multiple numbers which one do you want to change? Choose its id: ")
            while not checkInteger.is_integer(ans) or int(ans) <= 0 or int(ans) > len(numbers):
                ans = input("Please enter valid id: ")
        ans = int(ans)
        sql = "update people set Number = REPLACE(Number, %s, %s), Country = REPLACE(Country, %s, %s) WHERE Id = %s;"
        res = input(f"Are you sure to change {numbers[ans - 1]} number to +{number} number? (Y | N): ")
        if res == "Y" or res == "y":
            conn.cursor.execute(sql, (numbers[ans - 1][1:], number, countries[ans - 1], country, self.people[self.id]["Id"]))
            conn.connection.commit()
            print(f"{numbers[ans - 1]} changed to +{number} successfully")
            self.add_edit_history(numbers[ans - 1], "+" + number, self.address_book_name, self.address_book_id)
            numbers[ans - 1] = '+' + number
            countries[ans - 1] = country
            self.people[self.id]["Number"] = ",".join(numbers)
            self.people[self.id]["Country"] = ",".join(countries)
    
    def delete_person_edit(self) -> None:
        check = self.delete_person(self.people, self.id, self.address_book_name, self.address_book_id)
        if check:
            self.add_delete_history(self.people[self.id]["Name"], self.people[self.id]["Surname"], self.people[self.id]["Number"], self.people[self.id]["Country"], self.people[self.id]["Is_blocked"], self.address_book_name, self.address_book_id)

    def block_person_edit(self) -> None:
        self.block_unblock_person(self.people, self.id, self.address_book_name, self.address_book_id)

    def show_block_history_edit(self, address_book_name: str, address_book_id: int) -> None:
        sql = "select * from people where Is_blocked = %s and address_book = %s"
        conn.cursor.execute(sql, (True, address_book_id))
        blockedPeople = conn.cursor.fetchall()
        if len(blockedPeople) == 0:
            print("Nobody was blocked")
        else:
            for i in range(len(blockedPeople)):
                print(self.show_person(blockedPeople[i]["Name"], blockedPeople[i]["Surname"], blockedPeople[i]["Number"], blockedPeople[i]["Country"], i + 1, blockedPeople[i]["Is_blocked"], address_book_name))