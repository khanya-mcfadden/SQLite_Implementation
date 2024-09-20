import sqlite3

connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """INSERT INTO customer (FirstName, LastName, email, Phone) VALUES ('sam', 'mathews', 'samm@gmail.com', '501-346-439');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()



connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist
query = """INSERT INTO sale (productId, customerId, date, time) VALUES ('4','1','20/12/2024', '16:00');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()
