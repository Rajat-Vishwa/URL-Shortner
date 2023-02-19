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

To simply shorten a URL with a random back-half,

```python
    url = 'www.youtube.com'
    
    shortened_url = sh.shorten(url=url)

    print(shortened_url)
```

For a custom back-half,

```python
    url = 'www.youtube.com'
    bk_hlf = 'abcd'
    
    shortened_url = sh.shorten(url=url, custom_back_half=bk_hlf)

    print(shortened_url)  # None if the back-half is already taken
```

To manually generate a random back-half with custom size (say 5),

```python
    url = 'www.youtube.com'
    bk_hlf = sh.generate_backhalf(len=5)
    
    shortened_url = sh.shorten(url=url, custom_back_half=bk_hlf)

    print(shortened_url)
```