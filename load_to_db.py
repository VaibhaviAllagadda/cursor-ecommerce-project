
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS payments")
cur.execute("DROP TABLE IF EXISTS order_items")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("DROP TABLE IF EXISTS customers")

cur.execute('''
CREATE TABLE customers(
 customer_id INTEGER PRIMARY KEY,
 name TEXT,
 email TEXT,
 city TEXT
)
''')

cur.execute('''
CREATE TABLE products(
 product_id INTEGER PRIMARY KEY,
 name TEXT,
 category TEXT,
 price REAL
)
''')

cur.execute('''
CREATE TABLE orders(
 order_id INTEGER PRIMARY KEY,
 customer_id INTEGER,
 order_date TEXT,
 total_amount REAL,
 FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')

cur.execute('''
CREATE TABLE order_items(
 item_id INTEGER PRIMARY KEY,
 order_id INTEGER,
 product_id INTEGER,
 quantity INTEGER,
 FOREIGN KEY(order_id) REFERENCES orders(order_id),
 FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

cur.execute('''
CREATE TABLE payments(
 payment_id INTEGER PRIMARY KEY,
 order_id INTEGER,
 payment_method TEXT,
 status TEXT,
 amount REAL,
 FOREIGN KEY(order_id) REFERENCES orders(order_id)
)
''')

files = ["customers","products","orders","order_items","payments"]
for f in files:
    df = pd.read_csv(f"data/{f}.csv")
    df.to_sql(f, conn, if_exists="append", index=False)

conn.commit()
conn.close()
print("Database ecommerce.db created and data loaded.")
