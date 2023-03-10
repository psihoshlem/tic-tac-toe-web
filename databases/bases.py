import sqlite3

conn = sqlite3.connect('./databases/users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   login TEXT,
   password TEXT,
   salt TEXT);
""")
conn.commit()

def add_new_user(user: dict):
   user = (user["login"], user["password"], user["salt"])
   cur.execute("INSERT INTO users (login, password, salt) VALUES(?, ?, ?);", user)
   conn.commit()

# для входа
def get_user_data(login: str):
   cur.execute(f"select * from users where login='{login}'")
   password, salt = cur.fetchall()[0][2:]
   return password, salt


def is_user_exist(login: str):
   cur.execute(f"select * from users where login='{login}'")
   return cur.fetchall()!=[]
