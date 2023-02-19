# URL-Shortner

## OVERVIEW

This package can be used to generate random or custom short urls for urls and store them in a local database.
The server.py file is the server that is used to redirect the shortened urls to their corresponding destinations.

### Usage

Import the Shortner class,

```python
    from Shortner.shortner import Shortner
```

Create an instance of the Shortner,

```python
    sh = Shortner()
```

To simply shorten a URL with a random back-half (default length 4),

```python
    url = 'www.youtube.com'
    
    shortened_url = sh.shorten(url=url)

    print(shortened_url)
```

To manually generate a random back-half with custom size (say 5),

```python
    url = 'www.youtube.com'
    bk_hlf = sh.generate_backhalf(len=5)
    
    shortened_url = sh.shorten(url=url, custom_back_half=bk_hlf)

    print(shortened_url)
```

For a custom back-half,

```python
    url = 'www.youtube.com'
    bk_hlf = 'abcd'
    
    shortened_url = sh.shorten(url=url, custom_back_half=bk_hlf)

    print(shortened_url)  # None if the back-half is already taken
```


## Server
The server.py file handles all the requests and redirects the short url to its corresponding destination.
The server.py file needs to be run in order for the url to be redirected.


## User login feature
The shortner class provides the user to login with their registered username and password so that the urls they shorten can be stored with a tag (their username) so that they can view/delete their shortened urls.
The registered user data gets stored in the 'users' table of 'url_data.db'.

The class has following methods for this,

To register a new user,

```python
    def register(self, username: str, password: str):
        """ Register a new user in the 'users' table and automatically login

                Parameters:
                    username (str) : The username the user wants
                    password (str) : Password

                Returns:
                    True: if user successfully registered
                    False: if the username if already taken or already logged in
            """
 ```
 
 To login an existing user,
 
 ```python
    def login(self, username: str, password: str):
        """ Login an existing user 

                Parameters:    
                    username (str): The username of the existing user
                    password (str): Password

                Returns:
                    True: If logged in successfully
                    False: If the user does not exists
        """ 
```
 
 To remove a user account,
 
 ```python
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
```

To list all the urls a user(logged in) has shortened,

```python
    def list_urls(self):
        """ List all the urls shortened by a user (if logged in)

                Returns:
                    A list of tuples(short_url, long_url) containing all the urls shortened by a user 
            
                    None: If user not logged in
        """
```

To delete a shortened url,

```python
    def delete_url(self, url: str):
        """ Deletes a short url from the database if it exists(requires to be logged in)

            Parameters:
                url (str): The short url user wants to delete

            Returns:
                True: If url deleted successfully, or the short url doesn't exist
                False: If the user is not logged in
        """
```





