import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_basket_button_exists(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	button_basket = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
	assert button_basket > 0, 'selector is not found'

if __name__ == "__main__":
	pytest.main()

