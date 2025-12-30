import sqlite3
import os

db_path = "database/products.db"

if os.path.exists(db_path):
    os.remove(db_path)
    print("Database reset")

else:
    print("Database not found")
