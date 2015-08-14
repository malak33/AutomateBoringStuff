#! python3
# downloadWebPage.py - download a web page with the requests.get() function.
import requests
res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
type(res)
#res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])