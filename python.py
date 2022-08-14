from selenium import webdriver
from webdriver_manager.chrome import chromeDriverManager
email_id = input('enter username')
password = input('enter password')
server = webdriver.chrome(chromeDriverManager().install())
server.get('https://www.facebook.com')
user = server.get_element_by_id('email')
user.send_key(email_id)
passkey = server.get_element_by_id('pass')
passkey.send_key(password)
login = server.get_element_by_id('loginbutton')
ligin.click()
server.quit()

