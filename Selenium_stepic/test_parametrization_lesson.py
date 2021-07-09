import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_stepic_parametrs_lesson(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    input1 = browser.find_element_by_css_selector('[placeholder="Type your answer here..."]')
    input1.send_keys(answer)
    button1 = browser.find_element_by_css_selector('button.submit-submission')
    button1.click()
    otvet = browser.find_element_by_css_selector('pre.smart-hints__hint')
    correct_otvet = otvet.text
    assert correct_otvet == "Correct!", "Неправильный ответ"
