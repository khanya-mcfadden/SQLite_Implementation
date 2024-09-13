import sqlite3

connection = sqlite3.connect('customer.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """INSERT INTO customer (username, email, First_Name, Last_Name, address, Phone_Number) VALUES ('johndoe', 'john@gmail.com', 'John', 'Doe', '1234 Elm St', '555-555-5555');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()


connection = sqlite3.connect('sale.db', check_same_thread=False) #Will create DB if it doesn't already exist
query = """INSERT INTO sale (product id, customer id, date, timke) VALUES ('',);"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()
