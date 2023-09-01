import requests
import sqlite3
from datetime import datetime, timedelta
import random

def fetch_product_data(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(url)
    
    try:
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        product_data = response.json()
        return product_data
    except requests.exceptions.HTTPError as e:
        print(f"Error: Failed to fetch product data for ID {product_id}. {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error: Invalid JSON response for ID {product_id}. {e}")
    
    return None

def create_products_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            price REAL,
            description TEXT,
            date_added TEXT
        )
    ''')

def insert_product_into_db(cursor, product_data):
    title = product_data["title"]
    category = product_data["category"]
    price = product_data["price"]
    description = product_data["description"]
    date_added = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
    
    cursor.execute('''
        INSERT INTO products (title, category, price, description, date_added)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, category, price, description, date_added))

# Interactive version (Challenge)
start_id = int(input("Enter the starting product ID: "))
end_id = int(input("Enter the ending product ID: "))

# Connect to the database
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Create the products table
create_products_table(cursor)

# Fetch product data and insert into the database
for product_id in range(start_id, end_id + 1):
    product_data = fetch_product_data(product_id)
    if product_data:
        insert_product_into_db(cursor, product_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Product data retrieval and insertion completed successfully.")