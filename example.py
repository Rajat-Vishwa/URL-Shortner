from Shortner.shortner import Shortner

sh = Shortner()

#-------------------------------------------------------------------
# Register a new user

username = 'admin'
password = 'root'

if sh.register(username=username, password=password):
    print("User registered successfully.")
else: 
    print("Username not available")

#-------------------------------------------------------------------

#-------------------------------------------------------------------
# Login

if sh.login(username=username, password=password):
    print("Logged in successfully.")
else: 
    print("User doesn't exist")

#-------------------------------------------------------------------

#-------------------------------------------------------------------
# Check a back-half

bk_hlf = 'abcd'

if sh.check_back_half(back_half=bk_hlf):
    print("Back-half available")
else:
    print("Back-half not available")

#-------------------------------------------------------------------

# Custom back-half
bk_hlf = 'abcd'

url = 'https://youtu.be/dQw4w9WgXcQ'

short = sh.shorten(url=url, custom_back_half=bk_hlf)

if short:
    print('Custom shortened url is ', short)
else:
    print('Back-half not available')

#-------------------------------------------------------------------

# Random back-half
url = 'https://youtu.be/dQw4w9WgXcQ'

short = sh.shorten(url=url)

if short:
    print('Random shortened url is ', short)
else:
    print('Back-half not available')

#-------------------------------------------------------------------

# List user urls

print('\n')

urls = sh.list_urls()

print('Urls shortened are,')
for url in urls:
    print(url)
    sh.delete_url(url[0])



