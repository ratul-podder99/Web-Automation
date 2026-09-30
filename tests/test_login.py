"""
Login Test Suite - automationexercise.com

Covers the scenario required by the assessment:
    1. Launch the website.
    2. Navigate to the Login page.
    3. Enter the registered email address and password.
    4. Submit the login form.
    5. Verify that the login was successful.

Prerequisite: a real account must already exist on the site (created
manually per README.md, Step 1) and its credentials placed in .env.
"""

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:

    def test_successful_login_with_valid_credentials(self, driver, credentials):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        # 1. Launch the website
        home_page.load()
        assert "Automation Exercise" in driver.title

        # 2. Navigate to the Login page
        home_page.go_to_login()
        assert login_page.is_loaded(), "Login form did not load after clicking 'Signup / Login'."

        # 3 & 4. Enter registered email/password and submit the form
        login_page.login(credentials["email"], credentials["password"])

        # 5. Verify that the login was successful
        assert home_page.is_user_logged_in(), (
            "Login did not succeed: 'Logged in as <user>' indicator was not found. "
            "Double-check TEST_EMAIL / TEST_PASSWORD in your .env file match an "
            "account that was actually registered on the site."
        )

        logged_in_text = home_page.get_logged_in_username_text()
        assert "Logged in as" in logged_in_text

    def test_login_fails_with_invalid_credentials(self, driver):
        """
        Bonus/extra negative-path check (not required by the assessment, kept
        minimal): confirms the site's own error handling still works, which
        gives confidence that a passing positive test above is meaningful
        and not just a login page that always reports success.
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.load()
        home_page.go_to_login()
        login_page.login("not_a_real_user_12345@example.com", "wrong-password")

        assert login_page.has_error_message(), "Expected an error message for invalid credentials."
        assert not home_page.is_user_logged_in(timeout=2)
