import math
from math import log, sin
import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('[type="submit"]')
    button1.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = int(x_element.text)

    def calc(x):
        return str(math.log(abs(12*sin(x))))

    y = calc(x)

    input_1 = browser.find_element_by_css_selector('#answer')
    input_1.send_keys(y)

    button2 = browser.find_element_by_tag_name("button")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
