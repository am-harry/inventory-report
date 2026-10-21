import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

products = [
    ("Wireless mouse", 24.99, 40),
    ("USB-C cable", 9.50, 120),
    ("Mechanical keyboard", 89.00, 15),
    ("Webcam", 49.95, 0),
]

cursor.executemany(
    "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
    products,
)
conn.commit()

cursor.execute("SELECT COUNT(*) FROM products")
print(cursor.fetchone()[0], "rows in products")

conn.close()