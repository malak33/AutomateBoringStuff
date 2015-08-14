#! python3
# downloadWebPage.py - download a web page with the requests.get() function.
import requests
res=requests.get('https://automatetheboringstuff.com/chapter10/')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])