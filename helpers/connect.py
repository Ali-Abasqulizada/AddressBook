import mysql.connector
connection = mysql.connector.connect(host = "localhost", user = "root", password = "Ali636a#", database = "ADDRESS")
cursor = connection.cursor(dictionary = True)