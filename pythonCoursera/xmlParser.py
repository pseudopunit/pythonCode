import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

handler = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_686644.xml').read()

xmlParser = ET.fromstring(handler)
counts = xmlParser.findall('.//count')
count = 0
for elm in counts:
    count = count + int(elm.text)

print(count)