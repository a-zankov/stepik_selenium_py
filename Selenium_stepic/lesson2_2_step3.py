import math
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_eld = browser.find_element_by_css_selector('#num1')
    num1 = int(num1_eld.text)

    num2_eld = browser.find_element_by_css_selector('#num2')
    num2 = int(num2_eld.text)

    summa = str(num1 + num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)

    # Find and click Submit button
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла