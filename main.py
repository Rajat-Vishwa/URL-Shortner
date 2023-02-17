from Shortner.shortner import shortner

sh = shortner()

sh.login(username='rajat', password='vishwa')

print(sh.list_urls())

url = "www.instagram.com"
short = sh.shorten(url=url)
print(short)

print(sh.list_urls())

print(sh.list_urls())