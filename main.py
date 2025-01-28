# import sqlite3

import psycopg2

con = psycopg2.connect(
    database="bot", 
    user="bot", 
    password="bot", 
    host="localhost", 
    port=5432
    )



# con = sqlite3.connect('test.db')

cursor = con.cursor()


def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user1 (
            id SERIAL PRIMARY KEY,
            username VARCHAR(200) NOT NULL,
            age INTEGER )
    """)
    con.commit()


def insert_into(username, age):
    cursor.execute("""
    INSERT INTO user1 (username, age)
    VALUES (%s, %s)""", (username, age))
    con.commit()


def get_all_users():
    cursor.execute("SELECT * FROM user")
    con.commit()
    return cursor.fetchall()


create_table()
insert_into('testuser', 20)
print(get_all_users())


# update
# filter 
# LEETCODE SQL
