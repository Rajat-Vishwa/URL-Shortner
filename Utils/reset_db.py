"""
    This script creates the 'url_data.db' file and adds the urls table to it which contains all the url data.
"""

import sqlite3

connection = sqlite3.connect('url_data.db')

cursor = connection.cursor()

#Create database, reset if exists
drop = "DROP TABLE IF EXISTS urls"
create = """CREATE TABLE urls(username text, short_url text, long_url text)"""
select = "SELECT * FROM urls"
insert = """INSERT INTO urls VALUES("default", "hello", "world")"""

cursor.execute(drop)
cursor.execute(create)
cursor.execute(insert)
cursor.execute(select)

connection.commit()
res = cursor.fetchall()
print(res)
connection.close()