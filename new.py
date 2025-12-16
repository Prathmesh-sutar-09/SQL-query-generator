import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO users (name, age) VALUES
('Alice', 25),
('Bob', 30)
""")

conn.commit()
conn.close()