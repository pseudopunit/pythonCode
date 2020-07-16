import json
import urllib.request, urllib.parse, urllib.error
import pandas as pd
import ssl
import label as label

urldomain = 'http://py4e-data.dr-chuck.net/json?'
urlentry = input('enter address :')
params = dict()
params['address'] = urlentry
params['key'] = 42
url = urldomain + urllib.parse.urlencode(params)
print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

handler = urllib.request.urlopen(url, context=ctx)
data = handler.read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    goto: label

#print(json.dumps(js, indent=4))

print(js['results'][0]['place_id'])
label: print('exited')
