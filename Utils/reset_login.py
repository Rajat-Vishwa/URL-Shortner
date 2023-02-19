"""
    This script creates the 'users' table which contains all the user login data.
"""

import sqlite3

connection = sqlite3.connect('url_data.db')

cursor = connection.cursor()

#Create database, reset if exists
drop = "DROP TABLE IF EXISTS users"
create = """CREATE TABLE users(username text, password text)"""
select = "SELECT * FROM users"
insert = """INSERT INTO users VALUES("rajat", "vishwa")"""

cursor.execute(drop)
cursor.execute(create)
cursor.execute(insert)
cursor.execute(select)

connection.commit()
res = cursor.fetchall()
print(res)
connection.close()