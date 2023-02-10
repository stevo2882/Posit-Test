from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.ide_page import IDEPage


class BasePage:
    """Base page holds common elements found in Posit Cloud."""

    NEW_SPACE_BTN = (By.CSS_SELECTOR, "button.newSpace.menuItem")
    SPACE_MENU = (By.CSS_SELECTOR, ".spaceMenu.mobileSubsOnly")
    NEW_PROJECT_BTN = (By.CSS_SELECTOR, ".action.menuDropDown")
    NEW_RSTUDIO_BTN = (By.CSS_SELECTOR, ".action.newRStudioProject")
    GEN_MESSAGE = (By.CSS_SELECTOR, ".genMessage")

    def __init__(self, driver):
        """ "Initialize BasePage.

        :param driver: The webdriver to use.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def create_new_space(self):
        """Click the new space button."""
        self.wait.until(ec.presence_of_element_located(self.NEW_SPACE_BTN)).click()
        return NewSpaceModal(self.driver)

    def get_spaces(self):
        """Return a list of the space names from the nav menu."""
        return self.wait.until(ec.presence_of_element_located(self.SPACE_MENU)).text.splitlines()

    def create_new_rstudio_project(self):
        """Click the button to create a new project."""
        self.wait.until(ec.presence_of_element_located(self.NEW_PROJECT_BTN)).click()
        self.wait.until(ec.presence_of_element_located(self.NEW_RSTUDIO_BTN)).click()
        return IDEPage(self.driver)


class NewSpaceModal(BasePage):
    """New Space Modaal page object."""

    NEW_SPACE_NAME = (By.CSS_SELECTOR, "input[id='name']")
    CREATE_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_space_name(self, space_name):
        """Type space name into input field."""
        self.wait.until(ec.presence_of_element_located(self.NEW_SPACE_NAME)).send_keys(space_name)

    def click_create_button(self):
        """Click the create button."""
        self.wait.until(ec.presence_of_element_located(self.CREATE_BTN)).click()
