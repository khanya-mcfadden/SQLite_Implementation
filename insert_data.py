import sqlite3
import random
import faker
fake = faker.Faker()

connection = sqlite3.connect('BeanBrew.db', check_same_thread=False) #Will create DB if it doesn't already exist




def generate_random_customer():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email().split('@')[0] + '@example.com'
    phone = fake.phone_number()
    return (first_name, last_name, email, phone)

def generate_random_sale():
    product_id = random.randint(1, 10)  # Assuming product IDs range from 1 to 10
    customer_id = random.randint(1, 10)  # Assuming customer IDs range from 1 to 10
    date = fake.date(pattern="%d/%m/%Y")
    time = fake.time(pattern="%H:%M")
    return (product_id, customer_id, date, time)

def generate_random_product():
    product_name = fake.random_element(elements=[
        "Latte", "Espresso", "Cappuccino", "Americano", "Macchiato", "Mocha", "Flat White", "Affogato", "Iced Coffee", "Cold Brew",
        "Green Tea", "Black Tea", "Herbal Tea", "Chai Latte", "Matcha Latte", "Iced Tea", "Bubble Tea", "Lemonade", "Hot Chocolate", "Milkshake",
        "Blueberry Muffin", "Chocolate Muffin", "Banana Muffin", "Bran Muffin", "Corn Muffin", "Pumpkin Muffin", "Apple Muffin", "Carrot Muffin", "Lemon Poppy Seed Muffin", "Cranberry Muffin",
        "Turkey Sandwich", "Ham Sandwich", "Chicken Sandwich", "Veggie Sandwich", "BLT Sandwich", "Club Sandwich", "Grilled Cheese Sandwich", "Egg Salad Sandwich", "Tuna Sandwich", "Roast Beef Sandwich",
        "Cheesecake", "Chocolate Cake", "Carrot Cake", "Red Velvet Cake", "Lemon Cake", "Pound Cake", "Sponge Cake", "Angel Food Cake", "Bundt Cake", "Coffee Cake",
        "Chocolate Chip Cookie", "Oatmeal Raisin Cookie", "Peanut Butter Cookie", "Sugar Cookie", "Snickerdoodle", "Gingerbread Cookie", "Macaron", "Shortbread Cookie", "Biscotti", "Fortune Cookie",
        "Fudge Brownie", "Walnut Brownie", "Blondie", "Cheesecake Brownie", "Peanut Butter Brownie", "Mint Brownie", "Caramel Brownie", "Raspberry Brownie", "Marble Brownie", "Espresso Brownie",
        "Plain Bagel", "Everything Bagel", "Sesame Bagel", "Cinnamon Raisin Bagel", "Blueberry Bagel", "Poppy Seed Bagel", "Onion Bagel", "Garlic Bagel", "Salt Bagel", "Cheddar Bagel",
        "Butter Croissant", "Almond Croissant", "Chocolate Croissant", "Ham and Cheese Croissant", "Spinach and Feta Croissant", "Plain Croissant", "Raspberry Croissant", "Blueberry Croissant", "Apple Croissant", "Strawberry Croissant",
        "Strawberry Smoothie", "Banana Smoothie", "Mango Smoothie", "Berry Smoothie", "Green Smoothie", "Peach Smoothie", "Pineapple Smoothie", "Avocado Smoothie", "Protein Smoothie", "Detox Smoothie",
        "Granola Bar", "Protein Bar", "Fruit Bar", "Nut Bar", "Chocolate Bar", "Energy Bar", "Cereal Bar", "Yogurt Bar", "Oat Bar", "Seed Bar",
        "Greek Yogurt", "Vanilla Yogurt", "Strawberry Yogurt", "Blueberry Yogurt", "Peach Yogurt", "Mango Yogurt", "Coconut Yogurt", "Almond Yogurt", "Soy Yogurt", "Cashew Yogurt",
        "Apple", "Banana", "Orange", "Grapes", "Strawberries", "Blueberries", "Raspberries", "Blackberries", "Pineapple", "Mango",
        "Almonds", "Cashews", "Walnuts", "Pistachios", "Peanuts", "Hazelnuts", "Macadamia Nuts", "Brazil Nuts", "Pecans", "Chestnuts",
        "Cheddar Cheese", "Swiss Cheese", "Mozzarella Cheese", "Parmesan Cheese", "Brie Cheese", "Gouda Cheese", "Blue Cheese", "Feta Cheese", "Goat Cheese", "Provolone Cheese",
        "Sparkling Water", "Still Water", "Coconut Water", "Vitamin Water", "Flavored Water", "Mineral Water", "Spring Water", "Distilled Water", "Purified Water", "Alkaline Water",
        "Orange Juice", "Apple Juice", "Grape Juice", "Cranberry Juice", "Pineapple Juice", "Tomato Juice", "Carrot Juice", "Beet Juice", "Pomegranate Juice", "Mango Juice",
        "Potato Chips", "Tortilla Chips", "Pretzels", "Popcorn", "Cheese Puffs", "Corn Chips", "Veggie Chips", "Pita Chips", "Rice Cakes", "Crackers",
        "Chicken Soup", "Tomato Soup", "Minestrone Soup", "Clam Chowder", "Broccoli Cheddar Soup", "French Onion Soup", "Lentil Soup", "Miso Soup", "Beef Stew", "Chicken Noodle Soup"
    ])
    
    existing_products = [row[0] for row in connection.execute("SELECT productName FROM product").fetchall()]
    while product_name in existing_products:
        product_name = fake.random_element(elements=[
            "Latte", "Espresso", "Cappuccino", "Americano", "Macchiato", "Mocha", "Flat White", "Affogato", "Iced Coffee", "Cold Brew",
            "Green Tea", "Black Tea", "Herbal Tea", "Chai Latte", "Matcha Latte", "Iced Tea", "Bubble Tea", "Lemonade", "Hot Chocolate", "Milkshake",
            "Blueberry Muffin", "Chocolate Muffin", "Banana Muffin", "Bran Muffin", "Corn Muffin", "Pumpkin Muffin", "Apple Muffin", "Carrot Muffin", "Lemon Poppy Seed Muffin", "Cranberry Muffin",
            "Turkey Sandwich", "Ham Sandwich", "Chicken Sandwich", "Veggie Sandwich", "BLT Sandwich", "Club Sandwich", "Grilled Cheese Sandwich", "Egg Salad Sandwich", "Tuna Sandwich", "Roast Beef Sandwich",
            "Cheesecake", "Chocolate Cake", "Carrot Cake", "Red Velvet Cake", "Lemon Cake", "Pound Cake", "Sponge Cake", "Angel Food Cake", "Bundt Cake", "Coffee Cake",
            "Chocolate Chip Cookie", "Oatmeal Raisin Cookie", "Peanut Butter Cookie", "Sugar Cookie", "Snickerdoodle", "Gingerbread Cookie", "Macaron", "Shortbread Cookie", "Biscotti", "Fortune Cookie",
            "Fudge Brownie", "Walnut Brownie", "Blondie", "Cheesecake Brownie", "Peanut Butter Brownie", "Mint Brownie", "Caramel Brownie", "Raspberry Brownie", "Marble Brownie", "Espresso Brownie",
            "Plain Bagel", "Everything Bagel", "Sesame Bagel", "Cinnamon Raisin Bagel", "Blueberry Bagel", "Poppy Seed Bagel", "Onion Bagel", "Garlic Bagel", "Salt Bagel", "Cheddar Bagel",
            "Butter Croissant", "Almond Croissant", "Chocolate Croissant", "Ham and Cheese Croissant", "Spinach and Feta Croissant", "Plain Croissant", "Raspberry Croissant", "Blueberry Croissant", "Apple Croissant", "Strawberry Croissant",
            "Strawberry Smoothie", "Banana Smoothie", "Mango Smoothie", "Berry Smoothie", "Green Smoothie", "Peach Smoothie", "Pineapple Smoothie", "Avocado Smoothie", "Protein Smoothie", "Detox Smoothie",
            "Granola Bar", "Protein Bar", "Fruit Bar", "Nut Bar", "Chocolate Bar", "Energy Bar", "Cereal Bar", "Yogurt Bar", "Oat Bar", "Seed Bar",
            "Greek Yogurt", "Vanilla Yogurt", "Strawberry Yogurt", "Blueberry Yogurt", "Peach Yogurt", "Mango Yogurt", "Coconut Yogurt", "Almond Yogurt", "Soy Yogurt", "Cashew Yogurt",
            "Apple", "Banana", "Orange", "Grapes", "Strawberries", "Blueberries", "Raspberries", "Blackberries", "Pineapple", "Mango",
            "Almonds", "Cashews", "Walnuts", "Pistachios", "Peanuts", "Hazelnuts", "Macadamia Nuts", "Brazil Nuts", "Pecans", "Chestnuts",
            "Cheddar Cheese", "Swiss Cheese", "Mozzarella Cheese", "Parmesan Cheese", "Brie Cheese", "Gouda Cheese", "Blue Cheese", "Feta Cheese", "Goat Cheese", "Provolone Cheese",
            "Sparkling Water", "Still Water", "Coconut Water", "Vitamin Water", "Flavored Water", "Mineral Water", "Spring Water", "Distilled Water", "Purified Water", "Alkaline Water",
            "Orange Juice", "Apple Juice", "Grape Juice", "Cranberry Juice", "Pineapple Juice", "Tomato Juice", "Carrot Juice", "Beet Juice", "Pomegranate Juice", "Mango Juice",
            "Potato Chips", "Tortilla Chips", "Pretzels", "Popcorn", "Cheese Puffs", "Corn Chips", "Veggie Chips", "Pita Chips", "Rice Cakes", "Crackers",
            "Chicken Soup", "Tomato Soup", "Minestrone Soup", "Clam Chowder", "Broccoli Cheddar Soup", "French Onion Soup", "Lentil Soup", "Miso Soup", "Beef Stew", "Chicken Noodle Soup"
        ])
    
    product_description = fake.sentence()
    price = round(random.uniform(1.0, 100.0), 2)
    return (product_name, product_description, price)
        

 
for _ in range(10000):
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
    
    # # # Insert random product data
    # random_product = generate_random_product()
    # query = """INSERT INTO product (productName, productDescription, price) VALUES (?, ?, ?);"""
    # cursor = connection.cursor()
    # cursor.execute(query, random_product)
    # connection.commit()  # Commit the transaction
    # cursor.close()
