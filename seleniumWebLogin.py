#! python3
# seleniumWebLogin.py - opens gmail, and logs in to gmail account

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('account@gmail.com')
# I added the next two lines, to make the program work correctly.
emailElem.submit()
time.sleep(.500)
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('gmailPassword')
passwordElem.submit()
