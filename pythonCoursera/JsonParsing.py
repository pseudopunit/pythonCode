import json
import urllib.request, urllib.parse, urllib.error


handler = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_686645.json')
data = handler.read().decode()

info = json.loads(data)
com = info['comments']
countSum = 0
for item in com:
    countSum = countSum + int(item['count'])

print(countSum)