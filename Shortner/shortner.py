import sqlite3 
import string
import random

class Shortner:
    """ shortner class contains all the methods required to use the URL-Shortner

        Author: rajat_vishwa

    """

    def __init__(self):
        self._connect_to_database()
        self._loggedIn = False   # Whether the user is logged in to a valid account.
        self.host_url = "http://localhost:5000/{}"   # The host url template | Used to convert a back-half to valid URL



    def _connect_to_database(self):
        """ Connects to the database

            Returns:
                sqlite3.connection object
        """

        self.connection = sqlite3.connect('url_data.db')    # Connect to the database
        self.cursor = self.connection.cursor()     # Initialize the cursor
        return self.connection  



    def login(self, username: str, password: str):
        """ Login an existing user 

                Parameters:    
                    username (str): The username of the existing user
                    password (str): Password
                
                Returns:
                    True: If logged in successfully
                    False: If the user does not exists
        """ 

        query = "SELECT * FROM users WHERE username = ? AND password = ?"   # SQL query to check the creds 
        params = (username , password)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():  # If a row exists in the 'users' table with given creds
            self._loggedIn = True  
            self._username = username
            return f"=>Logged in as {username}"
        else:
            self._loggedIn = False
            return None


            
    def logout(self):
        """ Resets the user to default(not logged in)"""

        self._loggedIn = False
        self._username = None



    def register(self, username: str, password: str):
        """ Register a new user in the 'users' table and automatically login
            
                Parameters:
                    username (str) : The username the user wants
                    password (str) : Password

                Returns:
                    True: if user successfully registered
                    False: if the username if already taken or already logged in
            """

        if(self._loggedIn):
            return False

        query = "SELECT * FROM users WHERE username= ?"
        self.cursor.execute(query, (username,))

        if self.cursor.fetchone():
            return False
        else:
            query = "INSERT INTO users VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            self.login(username=username, password=password)
            return True


    def remove_user(self, username: str, password: str, delete_urls = False):
        """ Remove/delete the user account
            If delete_urls is set True, delete all of the users urls

                Parameters:
                    username (str): The username to be deleted
                    password (str): Password
                    delete_urls (bool) (optional): Whether to delete the users shortened urls

                Returns:
                    None
        """

        query = "DELETE FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        self.connection.commit()

        if delete_urls:
            query = "DELETE FROM urls WHERE username = ?"
            self.cursor.execute(query, (username,))
            self.connection.commit()
        return None



    def check_back_half(self, back_half: str):
        """ Checks if a back-half if available

                Returns:
                    True: If back-half is available
                    False: If back-half is already taken
        """

        query = "SELECT * FROM urls WHERE short_url= ?"
        params = (self.host_url.format(back_half),)
        self.cursor.execute(query, params)

        if self.cursor.fetchone():
            return False
        else:
            return True


    
    def generate_backhalf(self, len: int = 4):
        """ Generates a random back-half of a given length

                Parameters:
                    len (int): the length of the random string generated (default 4)

                Returns:
                    back_half (str): A random string of random letters (uppercase and lowercase) of given length
        """

        letters = string.ascii_letters
        random_str = ''.join(random.choice(letters) for i in range(len))
        if self.check_back_half(back_half=random_str):
            return random_str
        else:
            return self.generate_backhalf()



    def __add_to_database(self, long_url, short_url):
        # Add a url and its corresponding short url to the database

        # Add the url and the username of the user who added it
        # If not logged in, the username if set to 'default'
        username = self._username if self._loggedIn else 'default'  
        query = "INSERT INTO urls VALUES (?, ?, ?)"
        params = (username, short_url, long_url)
        self.cursor.execute(query, params)
        return self.connection.commit()



    def shorten(self, url: str, custom_back_half: str = None):
        """ Used to shorten a url and add it to the database
            
                Parameters:
                    url (str) : The url you want to shorten
                    custom_back_half (str) : The back half you want in the shortened url
                                            If not specified, generates a random back-half

                Returns: 
                    None: If a custom back-half is given and it is already taken
                    Shortened url (str): If the url is added to database successfully
        """

        if custom_back_half is not None:    # Check if the back-half is available
            if self.check_back_half(back_half=custom_back_half):
                shortened_url = self.host_url.format(custom_back_half)
            else:
                return None
        else: 
            back_half = self.generate_backhalf()
            shortened_url = self.host_url.format(back_half)   # Convert the back-half to a url using the host_url template
                
        self.__add_to_database(url, shortened_url)
        
        return shortened_url

            

    def list_urls(self):
        """ List all the urls shortened by a user (if logged in)

                Returns:
                    A list of tuples(short_url, long_url) containing all the urls shortened by a user 
            
                    None: If user not logged in
        """

        if self._loggedIn:
            query = "SELECT short_url, long_url FROM urls WHERE username = ?"
            self.cursor.execute(query, (self._username,))
            return self.cursor.fetchall()
        else:
            return None



    def delete_url(self, url: str):
        """ Deletes a short url from the database if it exists(requires to be logged in)

            Parameters:
                url (str): The short url user wants to delete

            Returns:
                True: If url deleted successfully, or the short url doesn't exist
                False: If the user is not logged in
        """

        if self._loggedIn:
            query = "DELETE FROM urls WHERE username = ? AND short_url = ?"
            self.cursor.execute(query, (self._username, url))
            self.connection.commit()
            return True
        else:
            return False
        