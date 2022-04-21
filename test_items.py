import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def test_button_is_here(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    text_button = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']").text
    assert len(text_button) > 0