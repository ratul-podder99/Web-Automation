"""
Shared pytest fixtures: WebDriver setup/teardown and credential loading.
"""

import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(0)  # explicit waits are used everywhere instead

    yield drv

    drv.quit()


@pytest.fixture
def credentials():
    """
    Reads the account created manually on automationexercise.com
    (see README.md, Step 1) from environment variables / .env file.
    """
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")
    if not email or not password:
        pytest.fail(
            "TEST_EMAIL / TEST_PASSWORD are not set. "
            "Copy .env.example to .env and fill in the account you "
            "manually registered on https://automationexercise.com/signup"
        )
    return {"email": email, "password": password}
