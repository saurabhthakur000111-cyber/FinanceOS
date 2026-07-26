import sqlite3
import os


DB_PATH = "financeos.db"


def get_connection():

    conn = sqlite3.connect(DB_PATH)

    return conn



def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS portfolio
        (
            id INTEGER PRIMARY KEY,
            symbol TEXT,
            quantity INTEGER,
            buy_price REAL
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analysis_history
        (
            id INTEGER PRIMARY KEY,
            symbol TEXT,
            analysis TEXT
        )
        """
    )


    conn.commit()

    conn.close()



if __name__ == "__main__":

    initialize_database()

    print(
        "Database initialized"
    )
def add_stock(symbol, quantity, buy_price):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO portfolio
        (
            symbol,
            quantity,
            buy_price
        )
        VALUES (?, ?, ?)
        """,
        (
            symbol,
            quantity,
            buy_price
        )
    )


    conn.commit()

    conn.close()



def get_portfolio():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM portfolio
        """
    )


    data = cursor.fetchall()


    conn.close()


    return data
