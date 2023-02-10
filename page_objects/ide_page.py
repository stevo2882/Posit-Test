from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class IDEPage:
    """IDE page holds common elements of the ide page."""

    CONSOLE = (By.ID, "rstudio_console_output")
    IFRAME = (By.CSS_SELECTOR, "#contentIFrame")
    WORKBENCH_FILES = (By.CSS_SELECTOR, "#rstudio_workbench_panel_files")
    WORKBENCH_ENV = (By.CSS_SELECTOR, "#rstudio_workbench_panel_environment")

    def __init__(self, driver):
        """Initialize the IDE Page."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.long_wait = WebDriverWait(self.driver, 30)

    def switch_to_iframe(self):
        """Wait for the IDE to load by checking for the existence of the IFrame."""
        iframe = self.long_wait.until(ec.presence_of_element_located(self.IFRAME))
        self.driver.switch_to.frame(iframe)

    def is_console_visible(self):
        """Return True if console is visible."""
        try:
            self.wait.until(ec.visibility_of_element_located(self.CONSOLE))
            return True
        except TimeoutException:
            return False

    def is_workbench_files_visible(self):
        """Return True if workbench is visible."""
        try:
            self.wait.until(ec.visibility_of_element_located(self.WORKBENCH_FILES))
            return True
        except TimeoutException:
            return False

    def is_workbench_environment_visible(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.WORKBENCH_ENV))
            return True
        except TimeoutException:
            return False
