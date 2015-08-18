#! python3
# - seleniumWebKeys.py - a short list of some other functions that will be used for selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)    # scrolls to the bottom
htmlElem.send_keys(Keys.HOME)   # scrolls to the top
browser.back()  # clicks the back bottom
browser.forward()   # clicks the forward bottom
browser.refresh()   # clicks the refresh button
browser.quit()  # clicks the close button