#author quanyin
#reference url:https://www.jianshu.com/p/ba02079ecd2f
from requests_html import HTMLSession
session = HTMLSession()
url = 'https://www.jianshu.com/p/85f4624485b9'
r = session.get(url)
print(r.html.text)
print('------------\n')
print(r.html.links)
print('------------\n')
print(r.html.absolute_links)