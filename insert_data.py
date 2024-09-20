import sqlite3
import random
import faker
fake = faker.Faker()

connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist




def generate_random_customer():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    return (first_name, last_name, email, phone)

def generate_random_sale():
    product_id = random.randint(1, 10)  # Assuming product IDs range from 1 to 10
    customer_id = random.randint(1, 10)  # Assuming customer IDs range from 1 to 10
    date = fake.date(pattern="%d/%m/%Y")
    time = fake.time(pattern="%H:%M")
    return (product_id, customer_id, date, time)
for _ in range(5):
    # Insert random customer data
    random_customer = generate_random_customer()
    query = """INSERT INTO customer (FirstName, LastName, email, Phone) VALUES (?, ?, ?, ?);"""
    cursor = connection.cursor()
    cursor.execute(query, random_customer)
    connection.commit()  # Commit the transaction
    cursor.close()

    # Insert random sale data
    random_sale = generate_random_sale()
    query = """INSERT INTO sale (productId, customerId, date, time) VALUES (?, ?, ?, ?);"""
    cursor = connection.cursor()
    cursor.execute(query, random_sale)
    connection.commit()  # Commit the transaction
    cursor.close()

connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist
query = """INSERT INTO sale (productId, customerId, date, time) VALUES ('4','1','20/12/2024', '16:00');"""
cursor = connection.cursor()
cursor.execute(query)
connection.commit()  # Commit the transaction
cursor.close()
