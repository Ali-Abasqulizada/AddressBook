from helpers import connect as conn
from helpers import checkInteger
class Address:
    def __init__(self) -> None:
        self.address = []
        self.id = 0
    
    def show_all_address(self) -> None:
        sql = "select * from address"
        conn.cursor.execute(sql)
        self.address = conn.cursor.fetchall()
        if len(self.address) == 0:
            print("There are not any Address Book")
            return
        for i in range(len(self.address)):
            print(self.show_address(self.address[i]["Name"], self.address[i]["Total"], i + 1))

    def delete_all_address(self) -> None:
        ans = input("Are you sure to delete all Address Books (That will delete all contacts you have)! (Y | N): ")
        if ans == "Y" or ans == "y":
            sql1 = "truncate table address"
            sql2 = "truncate table people"
            sql3 = "truncate table `delete`"
            sql4 = "truncate table edit"
            sql5 = "truncate table search"
            conn.cursor.execute(sql1)
            conn.cursor.execute(sql2)
            conn.cursor.execute(sql3)
            conn.cursor.execute(sql4)
            conn.cursor.execute(sql5)
            conn.connection.commit()
            print("Every single Address Book deleted!")

    def create_new_address(self, name: str) -> None:
        sql = "insert into Address (Name, Total) values(%s, %s)"
        try:
            conn.cursor.execute(sql, (name, 0))
            conn.connection.commit()
            print(f"New Address Book with '{name}' name is successfully added.")
        except:
            print(f"Address book with '{name}' name is already exists.")

    def show_address(self, name: str, total: int, id: int):
        return f"{id}. {name} ---> {total} {'people' if total > 1 else 'person'}"
    
    def enter_address(self) -> list:
        self.show_all_address()
        if len(self.address) == 0:
            return [False, False]
        ans = input("Please enter Id of Address Book that you want to enter: ")
        while not checkInteger.is_integer(ans) or int(ans) <= 0 or int(ans) > len(self.address):
            ans = input("Please enter valid id: ")
        self.id = int(ans) - 1
        print(f"'{self.address[self.id]["Name"]}' address book entered.")
        return [self.address[self.id]["Name"], self.address[self.id]["Id"]]
    
    def delete_address(self) -> None:
        self.show_all_address()
        if len(self.address) == 0:
            return
        ans = input("Please enter Id of Address Book that you want to delete: ")
        while not checkInteger.is_integer(ans) or int(ans) <= 0 or int(ans) > len(self.address):
            ans = input("Please enter valid id: ")
        self.id = int(ans) - 1
        check = input(f"Are you sure to delete '{self.address[self.id]["Name"]}' addess book? (Y | N): ")
        if check == "Y" or check == "y":
            sql1 = "Delete from address where Id = %s"
            sql2 = "Delete from people where address_book = %s"
            sql3 = "Delete from `delete` where address_book = %s"
            sql4 = "Delete from edit where address_book = %s"
            sql5 = "Delete from search where address_book = %s"
            conn.cursor.execute(sql1, (self.address[self.id]["Id"], ))
            conn.cursor.execute(sql2, (self.address[self.id]["Id"], ))
            conn.cursor.execute(sql3, (self.address[self.id]["Id"], ))
            conn.cursor.execute(sql4, (self.address[self.id]["Id"], ))
            conn.cursor.execute(sql5, (self.address[self.id]["Id"], ))
            conn.connection.commit()
            print(f"'{self.address[self.id]["Name"]}' address book deleted successfully.")