import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

link = 'http://selenium1py.pythonanywhere.com/'
end_link = '/catalogue/coders-at-work_207/'

def test_existence_of_add_to_cart_button(browser, lang):
    locale_link = link + lang + end_link
    browser.get(locale_link)
    time.sleep(10)

    assert browser.find_element(By.CLASS_NAME, "btn-primary"), "add to cart button not found"
