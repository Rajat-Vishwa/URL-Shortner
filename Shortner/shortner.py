import sqlite3
import string
import random

class shortner:

    def __init__(self):
        self.connect_to_database()
        self.loggedIn = False
        self.host_url = "localhost:5000/{}"
        self.back_half_len = 4


    def connect_to_database(self):
        self.connection = sqlite3.connect('url_data.db')
        self.cursor = self.connection.cursor()
        return self.connection


    def login(self, username: str, password: str):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        params = (username , password)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            self.loggedIn = True
            self.username = username
            return f"=>Logged in as {username}"
        else:
            self.loggedIn = False
            return None

            
    def logout(self):
        self.loggedIn = False
        self.username = None


    def register(self, username: str, password: str):
        if(self.loggedIn):
            return None

        query = "SELECT * FROM users WHERE username= ?"
        self.cursor.execute(query, (username,))

        if self.cursor.fetchone():
            return None
        else:
            query = "INSERT INTO users VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            self.login(username=username, password=password)
            return "Registered successfully"


    def check_back_half(self, back_half: str):
        query = "SELECT * FROM urls WHERE short_url= ?"
        params = (self.host_url.format(back_half),)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            return False
        else:
            return True

    
    def generate_backhalf(self, len: int = 4):
        letters = string.ascii_letters
        random_str = ''.join(random.choice(letters) for i in range(len))
        if self.check_back_half(back_half=random_str):
            return random_str
        else:
            return self.generate_backhalf()


    def __add_to_database(self, long_url, short_url):
        username = self.username if self.loggedIn else 'default'
        query = "INSERT INTO urls VALUES (?, ?, ?)"
        params = (username, short_url, long_url)
        self.cursor.execute(query, params)
        return self.connection.commit()


    def shorten(self, url: str, custom_back_half: str = None):
        if custom_back_half is not None:
            if self.check_back_half(back_half=custom_back_half):
                shortened_url = self.host_url.format(custom_back_half)
            else:
                return None
        else:
            back_half = self.generate_backhalf()
            shortened_url = self.host_url.format(back_half)

        self.__add_to_database(url, shortened_url)
        return shortened_url
            

    def list_urls(self):
        if self.loggedIn:
            query = "SELECT short_url, long_url FROM urls WHERE username = ?"
            self.cursor.execute(query, (self.username,))
            return self.cursor.fetchall()
        else:
            return None


    def delete_url(self, url: str):
        if self.loggedIn:
            query = "DELETE FROM urls WHERE username = ? AND short_url = ?"
            self.cursor.execute(query, (self.username, url))
            self.connection.commit()
        else:
            return None
        