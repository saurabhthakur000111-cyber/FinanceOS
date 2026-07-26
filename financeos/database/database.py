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
