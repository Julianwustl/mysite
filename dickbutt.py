import sqlite3
from sqlite3 import Error
import pandas as pd
import os

database = r"C:\Users\julia\Desktop\Python Programms\mysite"
excel = r"C:\Users\julia\Desktop\Python Programms\mysite\Marktdatenbank_added.xlsx"


source = os.path.join(os.path.dirname(__file__), "db.sqlite3")
df = pd.read_excel(excel)

with sqlite3.connect(source) as conn:

    cur = conn.cursor()
    print(cur.fetchall())
    df_db = pd.read_sql_query('select * from main_project', conn)
    dickbutt2 = df.columns.tolist()
    dickbutt = df_db.columns.tolist()
    print(dickbutt2)
    print(dickbutt)
    df.to_sql('main_project', conn, if_exists='append', index=False)
    print(df)


conn.execute('SELECT * from main_project').fetchall():