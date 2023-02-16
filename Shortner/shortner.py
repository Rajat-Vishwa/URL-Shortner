import sqlite3

class shortner:
    
    def __init__(self):
        self.connect_to_database()
        self.loggedIn = False


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

            
    def register(self, username, password):
        if(self.loggedIn):
            print("=>Already logged in")
            return

        query = "SELECT * FROM users WHERE username= ?"
        params = (username)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            print(f"=>Username already taken!")
        else:
            print("=>Username available")
            print("=>Adding user to database")
            query = "INSERT INTO users VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            self.login(username=username, password=password)

