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

def getCurrentDateTime():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    return date.strftime("%d/%m/%Y"), time.strftime("%X") 

def getProducts(): 
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall() 
    except sqlite3.Error as error:
        print("Database error:", error)
    finally: 
        cursor.close()
        
    print(products)
    return products

def joinTables():
    sales = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT Sale.id, Product.productName, Product.productDescription, Product.price,
                   Customer.firstName, Customer.lastName, Customer.email, Customer.Phone, 
                   Sale.date, Sale.time
            FROM Sale
            JOIN Product ON Sale.productID = Product.id
            JOIN Customer ON Sale.customerID = Customer.rowid
        """)
        sales = cursor.fetchall()
        print(f"Retrieved {len(sales)} sales records") 
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        cursor.close()
    return sales

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

@app.route('/add_records')
def edit_records():
        if request.method == "POST":

            record_type = request.form["record_type"]

            if record_type == "product":
                product_name = request.form["product_name"]
                product_description = request.form["product_description"]
                product_price = request.form["product_price"]

                cursor = connection.cursor()
                cursor.execute("INSERT INTO Product (productName, productDescription, price) VALUES (?, ?, ?)", (product_name, product_description, product_price))
                connection.commit()
                cursor.close()

            if record_type == "customer":
                first_name = request.form["first_name"]
                last_name = request.form["last_name"]
                email = request.form["email"]
                phone = request.form["phone"]

                cursor = connection.cursor()
                cursor.execute("INSERT INTO Customer (firstName, lastName, email, phone) VALUES (?, ?, ?, ?)", (first_name, last_name, email, phone))
                connection.commit()
                cursor.close()

            if record_type == "sale":
                product_id = request.form["product_id"]
                customer_id = request.form["customer_id"]
                date = request.form["date"]
                time = request.form["time"]

                cursor = connection.cursor()
                cursor.execute("INSERT INTO Sale (productID, customerID, date, time) VALUES (?, ?, ?, ?)", (product_id, customer_id, date, time))
                connection.commit()
                cursor.close()

            return redirect('/edit_records')


        if request.method == "GET":
          return render_template('edit_records.html')

@app.route('/products')
def products():
    products = getProducts()
    return render_template('products.html', products = products)

@app.route('/sales')
def sales():
    sales = joinTables()
    print(sales)
    return render_template('sales.html', sales=sales)

@app.route('/add_product')
def add_product():
    return render_template('add_product.html')


if __name__ == '__main__':
    app.run(debug = True)