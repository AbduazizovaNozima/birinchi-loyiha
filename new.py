
import sqlite3

con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT NOT NULL,
AGE INTEGER NOT NULL) 
""")

con.commit()

# Ma'lumot kiritish
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
con.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("UPDATE users SET age=? WHERE=?", (30,'Alice'))
con.commit()

con.close()











