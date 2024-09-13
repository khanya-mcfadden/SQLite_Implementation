import sqlite3

connection = sqlite3.connect('customer.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """INSERT INTO customer (username, email, First_Name, Last_Name, address, Phone_Number) VALUES ('johndoe', 'john@gmail.com', 'John', 'Doe', '1234 Elm St', '555-555-5555');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()


connection = sqlite3.connect('sales.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """CREATE TABLE IF NOT EXISTS sales(sale id, name, cost ,total) values 
    item name varchar(50) unique,
    num of sale varchar(100),
    cost per item varchar(50),
    total cost varchar(50)
);""" 
cursor = connection.cursor()
cursor.execute(query)
cursor.close()