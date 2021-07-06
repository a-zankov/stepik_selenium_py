import math
from math import log, sin
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Учимся работать с Git from Pycharm
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button777=browser.find_element_by_css_selector("#book")
    button777.click()

    x_element = browser.find_element_by_css_selector('#input_value')
    x = int(x_element.text)

    def calc(x):
        return str(math.log(abs(12*sin(x))))

    y = calc(x)

    input_1 = browser.find_element_by_css_selector('#answer')
    input_1.send_keys(y)

    button2 = browser.find_element_by_css_selector('#solve')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()