E-Commerce Synthetic Data Pipeline (Cursor IDE + SQLite + SQL)

This project demonstrates a complete AI-assisted SDLC workflow using Cursor IDE, Python, SQLite, and SQL to generate, process, and analyze synthetic e-commerce data.

Designed as part of an internship-style exercise, the project showcases skills in:

🧠 AI-assisted development (Cursor IDE)

🐍 Python scripting

🗃️ Database creation & ingestion (SQLite)

📊 SQL JOIN queries

🔄 End-to-end data engineering pipeline

💾 GitHub project management

🚀 Project Overview

This project generates synthetic e-commerce data, loads it into a SQLite database, and performs SQL analytics through multi-table joins.

It includes:

5 synthetic CSV datasets

SQLite database (ecommerce.db)

Python ETL scripts

SQL analytical queries

End-to-end automation using Cursor IDE

📂 Project Structure
cursor-ecommerce-project/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── payments.csv
│
├── generate_data.py      # Generate synthetic datasets
├── load_to_db.py         # Load CSVs into SQLite
├── join_query.sql        # SQL join query
├── run_query.py          # Execute SQL using Python
└── ecommerce.db          # SQLite database (auto-generated)

🧪 Dataset Details
1️⃣ Customers

customer_id

name

email

city

2️⃣ Products

product_id

name

category

price

3️⃣ Orders

order_id

customer_id

order_date

total_amount

4️⃣ Order Items

item_id

order_id

product_id

quantity

5️⃣ Payments

payment_id

order_id

payment_method

status

amount

⚙️ How to Run the Project
1. Install Dependencies
pip install pandas faker

2. Generate Synthetic Data
python generate_data.py

3. Create and Load SQLite Database
python load_to_db.py

4. Run the SQL Join Query

Via Python:

python run_query.py


Via SQL:

SELECT 
    o.order_id,
    c.name AS customer_name,
    p.name AS product_name,
    oi.quantity,
    p.price,
    o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
