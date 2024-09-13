import sqlite3
connection = sqlite3.connect('customer.db', check_same_thread=False) #Will create DB if it doesn't already exist

query = """CREATE TABLE IF NOT EXISTS product( Id integer [primary key]
  username varchar(50) unique
  email varchar(100) unique
  First_Name varchar(50)
  Last_Name varchar(50)
  address varchar(255) 
  Password_Hash varchar(255)
  Phone_Number varchar(255)
  created_At timestamp
  Updated_At timestamp);"""
cursor = connection.cursor()
cursor.execute(query)
cursor.close()