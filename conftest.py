import pytest
import os
from selenium import webdriver
import chromedriver_autoinstaller
from dotenv import load_dotenv
from page_objects.login_page import LoginPage

load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


@pytest.fixture()
def driver():
    """Returns a webdriver object to the calling test."""
    chromedriver_autoinstaller. install()
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture()
def login(driver):
    """Fixture for login."""
    login_page = LoginPage(driver)
    login_page.type_username(EMAIL)
    login_page.click_submit()
    login_page.type_password(PASSWORD)
    login_page.click_submit()
    login_page.click_posit_cloud_button()
