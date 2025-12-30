import sqlite3

conn = sqlite3.connect("database/products.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT source, title, old_price, new_price, scraped_at
    FROM price_history
""")

rows = cursor.fetchall()

print("TOTAL HISTORY ROWS:", len(rows))
for row in rows:
    print(row)

conn.close()
