import time

import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    time.sleep(5)
    request.cls.driver = driver
    yield
    print("Test ended...")
    driver.close()
