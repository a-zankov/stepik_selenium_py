import math
import time

from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    # Find input area end fill in the value
    input_1 = browser.find_element_by_css_selector('#answer')
    input_1.send_keys(y)

    # Find and click the checkbox
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    # Find and click the radiobutton
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    # Find and click Submit button
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла