import sqlite3

connection = sqlite3.connect('url_data.db')

cursor = connection.cursor()

#Create database, reset if exists
drop = "DROP TABLE IF EXISTS urls"
create = """CREATE TABLE urls(username text, short_url text, long_url text)"""
select = "SELECT * FROM urls"
insert = """INSERT INTO urls VALUES("rajat_vishwa", "hello", "world")"""

cursor.execute(drop)
cursor.execute(create)
#cursor.execute(insert)
cursor.execute(select)

connection.commit()
res = cursor.fetchall()
print(res)
connection.close()