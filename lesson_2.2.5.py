import os
from selenium import webdriver
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

first_name = browser.find_element_by_name('firstname')
last_name = browser.find_element_by_name('lastname')
email = browser.find_element_by_name('email')

first_name.send_keys('first_name')
last_name.send_keys('last_name')
email.send_keys('test@test.com')

file_to_send = open('test.txt', 'w+')

for i in range(10):
    file_to_send.write("This is line %d\r\n" % (i+1))

file_to_send.close()

file = browser.find_element_by_name('file')
file.send_keys(os.path.abspath(file_to_send.name))

submit = browser.find_element_by_css_selector('[type="submit"]')
submit.click()

time.sleep(10)
browser.quit()
