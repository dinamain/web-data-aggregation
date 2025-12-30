import sqlite3

conn = sqlite3.connect("database/products.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM price_history")
conn.commit()

conn.close()
print("price_history table cleared")
