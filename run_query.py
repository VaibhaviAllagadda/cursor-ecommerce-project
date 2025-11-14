import sqlite3
import pandas as pd

with sqlite3.connect("ecommerce.db") as con:
    df = pd.read_sql_query(open("join_query.sql").read(), con)
    print(df.head(10))
    print(f"\nRows returned: {len(df)}")