import sqlite3
from flask import Flask, redirect

host_url = 'localhost:5000/{}'  # The template for the shortened urls.

app = Flask(__name__)

@app.route('/')
def home():
    return "URL Shortner"


@app.route('/<short_url>')  # Get the back-half
def redirect_to_original(short_url):
    short_url = host_url.format(short_url)  # Convert the back-half to url

    query = f"SELECT long_url FROM urls WHERE short_url = ?"  # Get its corresponding long url.
    cursor.execute(query, (short_url,))

    res = cursor.fetchone()
    if res is not None: 
        long_url = res[0]
        if long_url.find("http://") != 0 and long_url.find("https://") != 0:  
            long_url = "https://" + long_url    # Complete the url if its not.
        return redirect(long_url)   # Redirect to the destination.
    else:
        return "URL not found"


def start_server():
    global connection, cursor
    connection = sqlite3.connect('url_data.db', check_same_thread=False)
    cursor = connection.cursor()
    app.run()
    

start_server()

