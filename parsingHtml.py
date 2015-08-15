#! python3
# - parsingHtml.py - an example on how to parse html webpages.

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStartchSoup = bs4.BeautifulStoneSoup(res.text)
type(noStartchSoup)

