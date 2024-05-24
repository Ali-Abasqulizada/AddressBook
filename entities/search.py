from helpers import connect as conn
from entities.person import Person
from entities.search_history import SeachHistory
class Search(Person, SeachHistory):
    def __init__(self) -> None:
        self.people = []

    def search(self, name: str, address_book_name: str, address_book_id: int) -> None:
        sql = f"select * from people where lower(name) like lower('{name}%') and address_book = {address_book_id}"
        conn.cursor.execute(sql)
        self.people = conn.cursor.fetchall()
        self.add_search_history(name, address_book_name, address_book_id)
        while len(self.people) == 0:
            ans = input(f"There is not a person in '{address_book_name}' address book with name '{name}'. Would you like try again? (Y | N): ")
            if ans == "Y" or ans == "y":
                name = input("Search a name: ")
                sql = f"select * from people where lower(name) like lower('{name}%') and address_book = {address_book_id}"
                conn.cursor.execute(sql)
                self.people = conn.cursor.fetchall()
                self.add_search_history(name, address_book_name, address_book_id)
            else:
                return {}, None
        for i in range(len(self.people)):
            print(self.show_person(self.people[i]["Name"], self.people[i]["Surname"], self.people[i]["Number"], self.people[i]["Country"], i + 1, self.people[i]["Is_blocked"], address_book_name))
        if __name__ != "__main__":
            return self.people, name