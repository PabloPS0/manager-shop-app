import sqlite3, os
from dotenv import load_dotenv

load_dotenv()
DATABASE_PATH = os.getenv('DATABASE_PATH')

class ProductNotFoundError(Exception):
    pass

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
    def delete(self, code):
        select_item = self.cursor.execute("SELECT * FROM produtos WHERE code = ?", (code)).fetchone()
        if select_item:
            self.cursor.execute("DELETE FROM produtos WHERE code = ?", (code))
            self.conn.commit()
        else:
            raise ProductNotFoundError(f"Produto com código {code} não encontrado.")
    def close_connection(self):
        # Método para fechar a conexão quando necessário
        self.conn.close()
