import pandas as pd
import sqlite3

# 1️⃣ Read CSV file
df = pd.read_csv("movies.csv")

# 2️⃣ Connect to SQLite database (or create new one)
conn = sqlite3.connect("movies.db")  # creates movies.db if it doesn't exist
cursor = conn.cursor()

# 3️⃣ Insert CSV into a table called 'movies'
# If table doesn't exist, pandas will create it automatically
df.to_sql("movies", conn, if_exists="replace", index=False)

# 4️⃣ Commit & Close
conn.commit()
conn.close()

print("CSV data inserted into 'movies' table in 'movies.db'!")
