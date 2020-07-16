import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# to ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def scrapper(s):
    handler = urllib.request.urlopen(s).read()
    soup2 = BeautifulSoup(handler, 'html.parser')
    return soup2


# Look at the parts of a tag
# 'TAG:',tag
# "URL:',tag.get('href', None)
# 'Contents:',tag.contents[0]
# 'Attrs:',tag.attrs

# link = http://py4e-data.dr-chuck.net/comments_686642.html
# tags = soup('span')
# count = 0
# sumS = 0
# for tag in tags:
#     sumS = sumS + int(tag.contents[0])
#     count = count + 1
#
# print(sumS)

times = int(input("enter how many time :"))
pos = int(input("enter position :"))
soup = scrapper('http://py4e-data.dr-chuck.net/known_by_Aiden.html')
tags = soup('a')

while times > 0:
    strg = tags[pos - 1].get('href', None)
    print(strg)
    soup = scrapper(strg)
    tags = soup('a')
    times = times - 1

print(re.findall('.+known_by_(.*)\.html', strg))

