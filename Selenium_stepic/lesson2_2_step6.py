import math
from math import log, sin
import time

from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = int(x_element.text)

    def calc(x):
        return str(math.log(abs(12*sin(x))))

    y = calc(x)

    input_1 = browser.find_element_by_css_selector('#answer')
    input_1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

