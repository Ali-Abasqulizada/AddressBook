# AddressBook
# Local Setup
1. Make sure you have python installed and MySQL database running.
2. Create database in local: mysql -u root -p
3. After you enter your password and log into MySQL, you'll be in the MySQL shell. From there, you can execute the source command to run your SQL script.
4. source database/reset.sql;
5. source database/main.sql;
6. Change password that is in helpers/connect.py.
7. Install dependencies: pip install -r requirements.
8. Run app.py file.
9. Note(If you want to run setup file you need to write below command in the terminal.)
10. pip install -e .
# Project Structure
1. entities folder contains modules that describe entities and their fields.
2. helpers folder contains helper modules like connect.py(used for to connect database) etc.
