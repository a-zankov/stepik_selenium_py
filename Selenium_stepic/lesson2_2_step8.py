from selenium import webdriver
import time

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    first_name.send_keys("John")
    last_name = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    last_name.send_keys("Doe")
    email = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    email.send_keys("www")

    text = browser.find_element_by_css_selector('[name="file"]')
    text.send_keys("D:/tableau_task.txt")

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
