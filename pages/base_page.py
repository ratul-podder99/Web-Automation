"""
Base Page
=========
Common Selenium helper methods shared by every page object.
Keeping waits/clicks/typing here means each page object only has to
declare its own locators and page-specific actions.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until an element is present, then return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return element

    def type_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Return True/False instead of raising, for use in assertions."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.find(locator, timeout).text
