import json
import urllib.request, urllib.parse, urllib.error
import ssl
import time

suma = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    url = 'https://blockchain.info/ticker'
    uh = urllib.request.urlopen(url, context=ctx)
    print('Retrieving', url)
except:
    print("----- Not possible to retrieve URL -----")
    exit()

while True:
    try:
        url = 'https://blockchain.info/ticker'
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()

    except:
        print("----- Not possible to retrieve URL -----")
        exit()
    #print('Retrieved', len(data), 'characters')

    try:
        info = json.loads(data)
        valorLast = info['USD']['last']
        print("Valor:", valorLast)
    except:
        print("----- Not possible to retrieve Data -----")
        exit()
        #info = None

    #if not info:
    #    print(' ==== Failure to Retrieve ====')

    #print(json.dumps(info, indent = 2))

    time.sleep(5)
#for item in info:
#    print('Valor:', float(item["USD"]["last"]))
    #print('Count', item["count"])
#print("Suma:", suma)
