import sqlite3, os
from dotenv import load_dotenv

load_dotenv()
DATABASE_PATH = os.getenv('DATABASE_PATH')

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE produtos(
code INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price REAL,
quantity INTEGER 
)''')
conn.commit()

conn.close()