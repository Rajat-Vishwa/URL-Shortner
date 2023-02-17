import sqlite3

connection = sqlite3.connect('url_data.db')

cursor = connection.cursor()

query = "SELECT short_url, long_url FROM urls WHERE username = 'default'"

cursor.execute(query)

#connection.commit()
res = cursor.fetchall()
print(res)
connection.close()