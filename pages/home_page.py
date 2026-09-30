"""
Home Page
=========
https://automationexercise.com/
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

BASE_URL = "https://automationexercise.com/"


class HomePage(BasePage):
    # Locators
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    LOGGED_IN_AS_INDICATOR = (By.XPATH, "//a[contains(text(), 'Logged in as')]")

    def load(self):
        self.open(BASE_URL)
        return self

    def go_to_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)
        return self

    def is_user_logged_in(self, timeout=10):
        """True if the 'Logged in as <name>' link is visible in the nav bar."""
        return self.is_visible(self.LOGGED_IN_AS_INDICATOR, timeout=timeout)

    def get_logged_in_username_text(self):
        return self.get_text(self.LOGGED_IN_AS_INDICATOR)
