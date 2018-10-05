# selenium02.py (facebook login)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth import Auth

auth = Auth('user_info.txt')
user_id = auth.get('user_id')
user_pwd = auth.get('user_pwd')

path = 'C:\\Work\\github\\python\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.facebook.com')

element = driver.find_element_by_name('email')
element.send_keys(user_id)
element = driver.find_element_by_name('pass')
element.send_keys(user_pwd)
element.send_keys(Keys.RETURN)
