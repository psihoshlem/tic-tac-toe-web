import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   login TEXT,
   password TEXT,
   salt TEXT);
""")
conn.commit()