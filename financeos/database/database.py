import sqlite3
from datetime import datetime


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("financeos.db")
        self.create_tables()


    def create_tables(self):

        query = """
        CREATE TABLE IF NOT EXISTS stocks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            price REAL,
            volume INTEGER,
            created_at TEXT
        )
        """

        self.connection.execute(query)
        self.connection.commit()


    def save_stock(self, symbol, price, volume):

        query = """
        INSERT INTO stocks
        (symbol, price, volume, created_at)
        VALUES (?, ?, ?, ?)
        """

        self.connection.execute(
            query,
            (
                symbol,
                price,
                volume,
                datetime.now()
            )
        )

        self.connection.commit()


    def fetch_all(self, query):

        cursor = self.connection.cursor()

        cursor.execute(query)

        return cursor.fetchall()