
import pandas as pd
from faker import Faker  # pyright: ignore[reportMissingImports]
import random
import os

fake = Faker()
os.makedirs("data", exist_ok=True)

# customers
customers = []
for i in range(1,51):
    customers.append([i,fake.name(),fake.email(),fake.city()])
pd.DataFrame(customers,columns=["customer_id","name","email","city"]).to_csv("data/customers.csv",index=False)

# products
products=[]
for i in range(1,51):
    products.append([i,fake.word(),random.choice(["Electronics","Clothing","Books","Home"]),round(random.uniform(10,5000),2)])
pd.DataFrame(products,columns=["product_id","name","category","price"]).to_csv("data/products.csv",index=False)

# orders
orders=[]
for i in range(1,51):
    cid=random.randint(1,50)
    amt=round(random.uniform(200,10000),2)
    orders.append([i,cid,fake.date_this_year(),amt])
pd.DataFrame(orders,columns=["order_id","customer_id","order_date","total_amount"]).to_csv("data/orders.csv",index=False)

# order_items
items=[]
for i in range(1,101):
    items.append([i,random.randint(1,50),random.randint(1,50),random.randint(1,5)])
pd.DataFrame(items,columns=["item_id","order_id","product_id","quantity"]).to_csv("data/order_items.csv",index=False)

# payments
payments=[]
for i in range(1,51):
    payments.append([i,i,random.choice(["UPI","Card","NetBanking"]),random.choice(["Success","Pending","Failed"]),round(random.uniform(200,10000),2)])
pd.DataFrame(payments,columns=["payment_id","order_id","payment_method","status","amount"]).to_csv("data/payments.csv",index=False)

print("Generated synthetic data in /data folder.")
