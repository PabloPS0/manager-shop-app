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
        select_item = self.cursor.execute("SELECT * FROM produtos WHERE code = ?", (code,)).fetchone()
        if select_item:
            self.cursor.execute("DELETE FROM produtos WHERE code = ?", (code,))
            self.conn.commit()
        else:
            raise ProductNotFoundError(f"Produto com código {code} não encontrado.")
    def search(self, code):
        product = self.cursor.execute("SELECT * FROM produtos WHERE code = ?", (code,)).fetchone()
        if product is None:
            raise ProductNotFoundError(f"Produto com código {code} não encontrado.")
        return product
    def update(self, name, price, quantity, code):
        product = self.cursor.execute("UPDATE produtos SET name = ?, price = ?, quantity = ? WHERE code = ?", (name, price, quantity, code))
        self.conn.commit()
        if self.cursor.rowcount == 0:
            raise ProductNotFoundError(f"Produto com código {code} não encontrado para atualização.")
        return f"Produto com código {code} atualizado com sucesso."
    def close_connection(self):
        # Método para fechar a conexão quando necessário
        self.conn.close()
