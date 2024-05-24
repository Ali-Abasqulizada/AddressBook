import mysql.connector
connection = mysql.connector.connect(host = "localhost", user = "root", password = "*", database = "ADDRESS")
cursor = connection.cursor(dictionary = True)