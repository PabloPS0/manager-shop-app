import sqlite3, os
from dotenv import load_dotenv

load_dotenv()
DATABASE_PATH = os.getenv('DATABASE_PATH')

class ProductRepository:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH) 
        self.cursor = self.conn.cursor()
    def add(self, name, price, quantity):
        self.cursor.execute('''INSERT INTO produtos (name, price, quantity) VALUES (?, ?, ?)''', (name, price, quantity))
        self.conn.commit()
    def list_all(self):
        self.cursor.execute('''SELECT * FROM produtos''')
        results = self.cursor.fetchall()
        return results
    def delete(self, name, price, quantity):
        self.cursor.execute('''DELETE FROM produtos WHERE nome = ? AND price = ? AND quantity = ?''')