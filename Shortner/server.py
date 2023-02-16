import mysql.connector
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "URL Shortner"

@app.route('/<short_url>')
def redirect_to_original(short_url):
    query = f"SELECT long_url FROM data WHERE short_url = {short_url}"
    cursor.execute(query)
    long_url = cursor.fetchone()
    if long_url is not None:
        return redirect(long_url)
    else:
        return "URL not found"


#connect to the database
def connect_to_database():
    global database, cursor
    try:
        database = mysql.connector.connect( host='localhost',
                                            user='root',
                                            password='vishwa',
                                            database='userdata')
    except Exception as e:
        print(e)

def start_server():
    try:
        connect_to_database()
        app.run()
    except Exception as e:
        print(e)
    
start_server()

