from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    """LoginPage holds the common elements of the login page."""

    URL = "https://login.posit.cloud/"
    USERNAME = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    POSIT_CLOUD_BTN = (By.CSS_SELECTOR, "a.appPicker.cloud.noLink")

    def __init__(self, driver):
        """Initialize the login page."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.URL)

    def type_username(self, username):
        """Type the username in the input field."""
        self.wait.until(ec.presence_of_element_located(self.USERNAME)).send_keys(username)

    def type_password(self, password):
        """Type the password in the input field."""
        self.wait.until(ec.presence_of_element_located(self.PASSWORD)).send_keys(password)

    def click_submit(self):
        """Click the submit button."""
        self.wait.until(ec.presence_of_element_located(self.SUBMIT_BTN)).click()

    def click_posit_cloud_button(self):
        """Click the Posit Cloud Button."""
        self.wait.until(ec.presence_of_element_located(self.POSIT_CLOUD_BTN)).click()
