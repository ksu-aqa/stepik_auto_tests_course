from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

browser.implicitly_wait(1)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

button = browser.find_element_by_id('book')
button.click()

x = int(browser.find_element_by_id('input_value').text)
root = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(root)

submit = browser.find_element_by_css_selector('[type="submit"]')
submit.click()

time.sleep(5)
browser.quit()
