from flask import Flask, render_template #Flask library and functions
import sqlite3 #Our database
import datetime #Used to display current date & time

#Instantiate Flask App
app = Flask(__name__)

#Connection to DB
connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist

#Set up table if it doesn't exist already
query = """CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, productName TEXT NOT NULL, productDescription TEXT NOT NULL, price REAL NOT NULL);"""
cursor = connection.cursor()
cursor.execute(query)
cursor.close() #Important to make sure we close the cursor when we are done with it.

def getCurrentDateTime():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    return date.strftime("%d/%m/%Y"), time.strftime("%X") #Format the date and time correctly before returning.

def getProducts(): #Query our table to retrieve all of our products
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall() #fetchone() vs fetchall() depending on the situation. We want all of the data here.
    except sqlite3.Error as error:
        print("Database error:", error)
    finally: #finally will always run after both a try and except. In other words: no matter if successful or not, this code will run.
        cursor.close()
        
    print(products)
    return products

def getsales(): #Query our table to retrieve all of our products
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sale")
        products = cursor.fetchall() #fetchone() vs fetchall() depending on the situation. We want all of the data here.
    except sqlite3.Error as error:
        print("Database error:", error)
    finally: #finally will always run after both a try and except. In other words: no matter if successful or not, this code will run.
        cursor.close()
        
    print(sale)
    return sale

#Starting (index) page & /home page are the same Note: You can use multiple routes attached to one function.
@app.route('/')
@app.route('/home')
def home():
    date, time = getCurrentDateTime()
    return render_template('home.html', date = date, time = time)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/products')
def products():
    products = getProducts()
    return render_template('products.html', products = products)

@app.route('/sales ')
def sales():
    sales = getSales()
    return render_template('sales.html', sales = sales)

#Run in debug mode.
if __name__ == '__main__':
    app.run(debug = True)