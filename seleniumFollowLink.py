#! python3
# seleniumFollowLink.py - opens a browser using selenium

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click()    # follows the "Read it Online" link
