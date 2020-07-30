import pytest
from selenium import webdriver

@pytest.fixture()
def web_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()