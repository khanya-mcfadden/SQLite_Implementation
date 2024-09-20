import sqlite3

connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """INSERT INTO customer (FirstName, LastName, email, Phone) VALUES ('John', 'Doe', 'john@gmail.com', '555-555-5555');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()




connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist
query = """INSERT INTO sale (productId, customerId, date, time) VALUES ('1','1','20/12/2024', '16:00');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()
