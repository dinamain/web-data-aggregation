import sqlite3
import logging

class DataStore:
    def __init__(self, db_path="database/products.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL,
                currency TEXT,
                scraped_at TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def insert_records(self, records):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT INTO products (title, price, currency, scraped_at)
            VALUES (?, ?, ?, ?)
        """, [
            (
                r["title"],
                r["price"],
                r["currency"],
                r["scraped_at"]
            ) for r in records
        ])

        conn.commit()
        conn.close()

        logging.info(f"Inserted {len(records)} records into database")
