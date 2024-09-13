import sqlite3
connection = sqlite3.connect('customer.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """CREATE TABLE IF NOT EXISTS customer(
    Id integer primary key,
    username varchar(50) unique,
    email varchar(100),
    First_Name varchar(50),
    Last_Name varchar(50),
    address varchar(255),
    Phone_Number varchar(255)
);"""  # Removed the trailing comma after Phone_Number column definition
cursor = connection.cursor()
cursor.execute(query)
cursor.close()

