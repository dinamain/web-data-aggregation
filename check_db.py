
import sqlite3

conn = sqlite3.connect("database/products.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]

print("Total records in DB:", count)

conn.close()
