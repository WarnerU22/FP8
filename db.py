import sqlite3

# Ensure table exists before app runs
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    preferred_contact TEXT
)
""")
conn.commit()
conn.close()


