#! python3
# seleniumOpenBrowser.py - opens a browser using selenium

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
