import bs4
import requests
import mechanize
import os
import http.cookiejar
##Kevin Phillips
##12/27/21
##Web scraping bot that will pull graddes from skyward
from urllib.request import urlopen

cook = http.cookiejar.LWPCookieJar()
#req = mechanize.Browser()
#req.set_cookiejar(cook)
payload={'login': os.eviron['SKYWARD_USERNAME'],'password': os.eviron['SKYWARD_PASSWORD'], "requestAction": "eel", "codeType": "tryLogin"}
resp1 = requests.post("https://skyward.alpinedistrict.org/scripts/wsisa.dll/WService=wsEAplus/skyporthttp.w", data=payload)
print(resp1.cookies)
print(resp1)

# req.open("https://skyward.alpinedistrict.org/scripts/wsisa.dll/WService=wsEAplus/seplog01")

# req.select_form(nr=0)
# req.form['login'] = 'SKYWARD_USERNAME'
# req.form['password'] = 'SKYWARD_PASSWORD'
# req.submit
# print(req.response().read())
print(cook._cookies)
#ARRRRRRRRRRRRRRGH
 