import sqlite3
import logging

class DataStore:
    def __init__(self, db_path="database/products.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    # ---------- PRODUCTS (LATEST SNAPSHOT) ----------

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                title TEXT NOT NULL,
                price REAL,
                currency TEXT,
                scraped_at TEXT NOT NULL,
                UNIQUE (source, title)
            );
        """)

        conn.commit()
        conn.close()

    # ---------- PRICE HISTORY ----------

    def create_price_history_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                title TEXT NOT NULL,
                old_price REAL,
                new_price REAL,
                change_percent REAL,
                scraped_at TEXT NOT NULL
            );
        """)

        conn.commit()
        conn.close()

    # ---------- INSERT / UPSERT ----------

    def insert_records(self, records):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT INTO products (source, title, price, currency, scraped_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(source, title) DO UPDATE SET
                price = excluded.price,
                currency = excluded.currency,
                scraped_at = excluded.scraped_at
        """, [
            (
                r["source"],
                r["title"],
                r["price"],
                r["currency"],
                r["scraped_at"]
            ) for r in records
        ])

        conn.commit()
        conn.close()

        logging.info(f"Upserted {len(records)} records into products")

    # ---------- SNAPSHOT FOR COMPARISON ----------

    def get_all_latest_prices(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT source, title, price FROM products
        """)

        data = {(row[0], row[1]): row[2] for row in cursor.fetchall()}
        conn.close()
        return data

    # ---------- HISTORY INSERT ----------

    def insert_price_change(self, record):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO price_history
            (source, title, old_price, new_price, change_percent, scraped_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            record["source"],
            record["title"],
            record["old_price"],
            record["new_price"],
            record["change_percent"],
            record["scraped_at"]
        ))

        conn.commit()
        conn.close()
