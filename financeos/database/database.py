"""
FinanceOS Database Module
"""

import sqlite3
from pathlib import Path


class Database:

    def __init__(self):
        self.db_path = Path("financeos.db")

    def connect(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL,
            volume INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        connection.commit()
        connection.close()

    def save_stock(self, symbol, price, volume):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO stocks(symbol, price, volume)
        VALUES (?, ?, ?)
        """, (symbol, price, volume))

        connection.commit()
        connection.close()

        print(f"{symbol} data saved successfully.")
