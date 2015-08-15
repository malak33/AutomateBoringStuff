#! python3
# - parsingFile.py - an example on how to download a webpage to a file, and then parse it.

import requests, bs4
res = requests.get('http://nostarch.com/automatestuff/')
res.raise_for_status()
playFile = open('example.html', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('p')
type(elems)
len(elems)
type(elems[0])
print(elems[0].getText())
str(elems[0])
#print(elems)
elems[0].attrs
