import sqlite3
import string
import random

class shortner:
    
    def __init__(self):
        self.connect_to_database()
        self.loggedIn = False
        self.host = "localhost:5000/{}"


    def connect_to_database(self):
        self.connection = sqlite3.connect('url_data.db')
        self.cursor = self.connection.cursor()
        print("=>Successfully connected to database.")
        return self.connection


    #Existing user login
    def login(self, username: str, password: str):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        params = (username , password)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            self.loggedIn = True
            self.username = username
            print(f"=>Logged in as {username}")
            return True
        else:
            self.loggedIn = False
            print("=>User does not exit, try register method to register or skip login.")
            return False

            
    def register(self, username: str, password: str):
        if(self.loggedIn):
            print("=>Already logged in")
            return

        query = "SELECT * FROM users WHERE username= ?"
        self.cursor.execute(query, (username,))

        if self.cursor.fetchone():
            print(f"=>Error while registering, username already taken!")
            return False
        else:
            print("=>Username available")
            print("=>Adding user to database")
            query = "INSERT INTO users VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            self.login(username=username, password=password)
            return True


    def check_back_half(self, back_half: str):
        query = "SELECT * FROM urls WHERE short_url= ?"
        params = (self.host.format(back_half),)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            print("=>Back-half not available")
            return False
        else:
            print("=>Back-half available")
            return True

    
    def generate_backhalf(self, len: int = 5):
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
                shortened_url = self.host.format(custom_back_half)
            else:
                return None
        else:
            back_half = self.generate_backhalf()
            shortened_url = self.host.format(back_half)

        self.__add_to_database(url, shortened_url)
        #print(f"Shortened url is {self.shortened_url}")
        return shortened_url
            
            