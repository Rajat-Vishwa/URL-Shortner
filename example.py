from Shortner.shortner import shortner

sh = shortner()

sh.login(username='rajat', password='vishwa')



url = "www.instagram.com"
short = sh.shorten(url=url)

print(sh.list_urls())

print(sh.delete_url(url='hehe'))

print(sh.list_urls())
