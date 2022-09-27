import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = 0

while count < 7:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    links = list()
    for tag in tags:
        link = tag.get('href', None)
        links.append(link)
    count += 1
    # print(count, links[17])
    url = links[17]
    # print(url)

nameurl = links[17].split('_')
nameurl = nameurl[2].split('.')
print(nameurl[0])
