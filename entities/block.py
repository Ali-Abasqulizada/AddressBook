from helpers import connect as conn
class Block:
    def __init__(self) -> None:
        self.people = []
        self.id = 0

    def block_unblock_person(self, people: list, id: int, address_book_name: str, address_book_id: int) -> None:
        self.people = people
        self.id = id
        if len(self.people) == 1:
            self.id = 0
        sql = "select * from people where Is_blocked = %s and address_book = %s"
        conn.cursor.execute(sql, (True, address_book_id))
        BlockedPeople = conn.cursor.fetchall()
        check = []
        for per in BlockedPeople:
            check.append(per["Id"])
        if self.people[self.id]["Id"] not in check:
            ans = input(f"Are you sure to block '{self.people[self.id]["Name"]} {self.people[self.id]["Surname"]}' in '{address_book_name}' address book? (Y | N): ")
            if ans == "Y" or ans == "y":
                sql = "update people set Is_blocked = %s where Id = %s"
                conn.cursor.execute(sql, (True, self.people[self.id]["Id"]))
                conn.connection.commit()
                print(f"'{self.people[self.id]["Name"]} {self.people[self.id]["Surname"]}' in '{address_book_name}' address book is blocked successfully")
        else:
            ans = input(f"'{self.people[self.id]["Name"]} {self.people[self.id]["Surname"]}' in '{address_book_name}' address book is already blocked. Do you want to unblock? (Y | N): ")
            if ans == "Y" or ans == "y":
                sql = "update people set Is_blocked = %s where Id = %s"
                conn.cursor.execute(sql, (False, self.people[self.id]["Id"]))
                conn.connection.commit()
                print(f"'{self.people[self.id]["Name"]} {self.people[self.id]["Surname"]}' in '{address_book_name}' address book is unblocked successfully")