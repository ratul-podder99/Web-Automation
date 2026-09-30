"""
Login Page
==========
https://automationexercise.com/login

The site marks its form inputs with stable "data-qa" attributes
(used across its own public API/UI test documentation), so locators
are built on those rather than on CSS classes, which are more likely
to change with styling updates.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    LOGIN_FORM_HEADING = (By.XPATH, "//h2[text()='Login to your account']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    def is_loaded(self, timeout=10):
        return self.is_visible(self.LOGIN_FORM_HEADING, timeout=timeout)

    def enter_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def submit(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, email, password):
        """Convenience method: fill both fields and submit in one call."""
        self.enter_email(email)
        self.enter_password(password)
        self.submit()
        return self

    def has_error_message(self, timeout=5):
        return self.is_visible(self.ERROR_MESSAGE, timeout=timeout)
