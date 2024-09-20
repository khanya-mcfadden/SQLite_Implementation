from flask import Flask, render_template, redirect, render_template, request 
import sqlite3 
import datetime 

app = Flask(__name__)

connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) 
query = """CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, productName TEXT NOT NULL, productDescription TEXT NOT NULL, price REAL NOT NULL);"""
cursor = connection.cursor()
cursor.execute(query)
cursor.close()

query = """CREATE TABLE IF NOT EXISTS customer(CustomerID INTEGER PRIMARY KEY, firstName TEXT NOT NULL, lastName TEXT NOT NULL, email TEXT NOT NULL, Phone TEXT NOT NULL);"""
cursor = connection.cursor()
cursor.execute(query)
cursor.close()

query = """CREATE TABLE IF NOT EXISTS sale(id INTEGER PRIMARY KEY, productID INTEGER NOT NULL, customerID INTEGER NOT NULL, date TEXT NOT NULL, time TEXT NOT NULL, FOREIGN KEY(productID) REFERENCES product(id), FOREIGN KEY(customerID) REFERENCES customer(id));"""
cursor = connection.cursor()
cursor.execute(query)
cursor.close()