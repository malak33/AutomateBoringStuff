#! python3
# seleniumFindClass.py - opens a browser using selenium

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find a element with that name.')
