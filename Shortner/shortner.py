import sqlite3

class shortner:
    
    def __init__(self):
        self.connect_to_database()
        self.loggedIn = False
        self.host = "127.0.0.1/5000/{}"

    def connect_to_database(self):
        self.connection = sqlite3.connect('url_data.db')
        self.cursor = self.connection.cursor()
        print("=>Successfully connected to database.")


    #Existing user login
    def login(self, username: str, password: str):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        params = (username , password)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            self.loggedIn = True
            self.username = username
            print(f"=>Logged in as {username}")
        else:
            self.loggedIn = False
            print("=>User does not exit, try register method to register or skip login.")

            
    def register(self, username: str, password: str):
        if(self.loggedIn):
            print("=>Already logged in")
            return

        query = "SELECT * FROM users WHERE username= ?"
        self.cursor.execute(query, (username,))

        if self.cursor.fetchone():
            print(f"=>Error while registering, username already taken!")
        else:
            print("=>Username available")
            print("=>Adding user to database")
            query = "INSERT INTO users VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            self.login(username=username, password=password)


        def check_back_half(self, back_half: str):
            query = "SELECT * FROM urls WHERE short_url= ?"
            params = (self.host.format(back_half),)
            self.cursor.execute(query, params)

            if not self.cursor.fetchone():
                print("=>Back-half not available")
                return False
            else:
                return True
            pass


        def shorten(self, url: str, custom_back_half: str = None):
            if custom_back_half is not None:
                if check_back_half(back_half=custom_back_half):
                    pass
            