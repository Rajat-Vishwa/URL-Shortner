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


#### User login feature
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
