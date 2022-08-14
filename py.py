from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

drivers = webdriver.Firefox()
drivers.get('https://web.whatsapp.com/')
time.sleep(10)
assert 'WhatsApp' in drivers.title
names = ['Du8']
for user in names:
    elem = drivers.find_element(By.XPATH, '//span[@title="{}"]'.format(user))
    elem.click()
    time.sleep(5)
"""elem.send_keys(Keys.RETURN)
elem.drivers.find_element(By.TITLE, 'Type a message')
elem.send_keys('hey there')
elem.send_keys(Keys.RETURN)"""
#drivers.close()
