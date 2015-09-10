from application import Application
from selenium import webdriver
import pytest


@pytest.fixture
def app(request):
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return Application(driver)

