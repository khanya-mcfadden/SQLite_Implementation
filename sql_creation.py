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
);""" 
cursor = connection.cursor()
cursor.execute(query)
cursor.close()
connection = sqlite3.connect('sale.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """CREATE TABLE IF NOT EXISTS sale(id INTEGER PRIMARY KEY, productID INTEGER NOT NULL, customerID INTEGER NOT NULL, date TEXT NOT NULL, time TEXT NOT NULL, FOREIGN KEY(productID) REFERENCES product(id), FOREIGN KEY(customerID) REFERENCES customer(id));"""
cursor = connection.cursor()
cursor.execute(query)
cursor.close()

