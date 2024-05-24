from helpers import connect as conn
from entities.number import Number
from entities.country import Country
from datetime import datetime

class Person(Number, Country):
    def __init__(self) -> None:
        self.first_name = "unknown"
        self.second_name = "unknown"
        self.number = "unknown"
        self.country = "unknown"
        self.address_book_name = "unknown"
        self.address_book_id = "unknown"
    def __str__(self) -> str:
        return self.show_person(self.first_name, self.second_name, self.number, self.country, 0, self.address_book_name, self.address_book_id)

    def add_person(self, name: str, surname: str, number: str, address_book_name: str, address_book_id: int) -> None:
        sql = "insert into People (Name, Surname, Number, Country, Is_blocked, address_book) values(%s, %s, %s, %s, %s, %s)"
        sql2 = "update address set Total = Total + 1 where Id = %s"
        self.first_name = name
        self.last_name = surname
        self.number = number
        self.address_book_name = address_book_name
        self.address_book_id = address_book_id
        while not self.check_number(self.number):
            self.number = input("please enter number: ")
        self.country = self.check_country(self.number)
        try:
            conn.cursor.execute(sql, (self.first_name, self.last_name, "+" + self.number, self.country, False, self.address_book_id))
            conn.cursor.execute(sql2, (address_book_id, ))
            print(f"'{self.first_name} {self.last_name}' added successfully to '{self.address_book_name}' Address Book")
        except:
            ans = input(f"{self.first_name} {self.last_name} is already in '{self.address_book_name}' Address Book. Do you want to add +{self.number}? (Y | N): ")
            if ans == "Y" or ans == "y":
                sql = "update people set Number = CONCAT(Number, ',', %s), Country = CONCAT(Country, ',', %s) where Name = %s AND Surname = %s AND address_book = %s"
                conn.cursor.execute(sql, ("+" + self.number, self.country, self.first_name, self.last_name, self.address_book_id))
                print(f"+{self.number} added to {self.first_name} {self.last_name} successfully")
        conn.connection.commit()
    
    def delete_all_people(self, address_book_name: str, address_book_id: int) -> None:
        ans = input(f"Are you sure to delete all contacts from '{address_book_name}' address book! (Y | N): ")
        if ans == "Y" or ans == "y":
            sql1 = "delete from people where address_book = %s"
            sql2 = "select * from people where address_book = %s"
            sql3 = "update address set Total = 0 where Id = %s"
            conn.cursor.execute(sql2, (address_book_id, ))
            people = conn.cursor.fetchall()
            conn.cursor.execute(sql1, (address_book_id, ))
            conn.cursor.execute(sql3, (address_book_id, ))
            for per in people:
                sql3 = "insert into `delete` (Info, Date, address_book) values (%s, %s, %s)"
                is_blocked = True if per["Is_blocked"] else False
                info = f"{per["Name"]} - {per["Surname"]} - {per["Number"]} - {per["Country"]} - {is_blocked} - {address_book_name}"
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                conn.cursor.execute(sql3, (info, time, address_book_id))
            conn.connection.commit()
            print(f"All people deleted from '{address_book_name}' address book successfully!")

    def show_person(self, name: str, surname: str, number: str, country: str, id: int, blocked: bool, address_book_name: str) -> str:
        return f'''
    ================= {id} ================
    Name: {name}
    Surname: {surname}
    Number: {number}
    Country: {country}
    Address Book: {address_book_name}
    =====================================
    {"Blocked" if blocked == True or blocked == "1" else ""}
    '''

    def show_all_people(self, address_book_name: str, address_book_id: int) -> None:
        sql = "select * from people where address_book = %s order by name"
        conn.cursor.execute(sql, (address_book_id, ))
        people = conn.cursor.fetchall()
        if len(people) == 0:
            print(f"'{address_book_name}' address book is empty")
        else:
            for i in range(len(people)):
                print(self.show_person(people[i]["Name"], people[i]["Surname"], people[i]["Number"], people[i]["Country"], i + 1, people[i]["Is_blocked"], address_book_name))