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
   print(cur.fetchall())


def is_user_exist(login: str):
   cur.execute(f"select * from users where login='{login}'")
   return cur.fetchall()!=[]

def delete_user_by_admin(login: str):
   cur.execute(f"DELETE FROM users WHERE lname='{login}';")
   conn.commit()


def delete_user_by_admin(user: dict):
   pass


# get_user_data()
# cur.execute(f"select * from users")
# for item in cur.fetchall():
#    print(item[1])

users = [
'senks',
'root',
'admin',
'no_exist'
]

for user in users:
   print(is_user_exist(user))