from entities.person import Person
from entities.address import Address
from helpers import connect as conn
from helpers.countries import country_codes
PER = Person()
AD = Address()
from faker import Faker
import random
sql = "select * from address"
conn.cursor.execute(sql)
addressBooks = conn.cursor.fetchall()
if not addressBooks:
    addressBooks = [{'Id': 1, 'Name': 'Family', 'Total': 0}, {'Id': 2, 'Name': 'Work', 'Total': 0}]
    AD.create_new_address("Family")
    AD.create_new_address("Work")
country_codes = list(country_codes.values())
for _ in range(50):
    name = Faker().first_name()
    surname = Faker().last_name()
    countryCode = random.choice(country_codes)
    number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    addressBook = random.choice(addressBooks)
    phone_number = f"{countryCode}{number}"
    PER.add_person(name, surname, phone_number, addressBook["Name"], addressBook["Id"])