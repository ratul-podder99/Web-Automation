# Automation Exercise - Login Test Automation

Selenium + Python (pytest) automation project that logs in to
[automationexercise.com](https://automationexercise.com/) with a
registered account and verifies the login succeeded.

Built with the **Page Object Model (POM)** pattern: page structure/locators
are isolated in `pages/`, test logic and assertions live in `tests/`.

## Project structure

```
automationexercise_project/
├── pages/
│   ├── base_page.py      # shared Selenium helpers (waits, click, type)
│   ├── home_page.py      # home page: load site, open login, read "Logged in as ..."
│   └── login_page.py     # login page: fill form, submit, read error message
├── tests/
│   └── test_login.py     # the required scenario + one bonus negative test
├── conftest.py            # pytest fixtures: WebDriver setup/teardown, credentials
├── requirements.txt
├── pytest.ini
├── .env.example           # template for your real credentials (not committed)
└── .gitignore
```

## Prerequisites

- Python 3.9+
- Google Chrome installed
- Internet access to automationexercise.com

`webdriver-manager` automatically downloads the correct ChromeDriver
version for your installed Chrome - no manual driver setup needed.

## Setup

1. **Manually create an account on the site first** (this step is
   intentionally manual, per the assessment instructions - do not
   automate signup):
   - Go to <https://automationexercise.com/signup>
   - Register with a real name/email and a password you'll reuse below.
   - Confirm you can see "Account Created!" and are logged in.

2. **Clone/open this project, then create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Add your credentials:**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set:

   ```
   TEST_EMAIL=the_email_you_registered_with@example.com
   TEST_PASSWORD=the_password_you_registered_with
   HEADLESS=false
   ```

   `.env` is git-ignored - your credentials are never committed.

## Running the tests

```bash
pytest
```

This runs both tests in `tests/test_login.py`:

- `test_successful_login_with_valid_credentials` - the required scenario
  (launch site → go to Login → enter registered email/password → submit →
  verify "Logged in as `<name>`" appears in the nav bar).
- `test_login_fails_with_invalid_credentials` - a bonus check confirming
  the site's own error message appears for bad credentials, which gives
  confidence the positive test above is actually validating something.

To run only the required scenario:

```bash
pytest tests/test_login.py::TestLogin::test_successful_login_with_valid_credentials
```

To run headless (no visible Chrome window, e.g. in CI):

```bash
HEADLESS=true pytest
```

## Design notes

- **Explicit waits only.** `implicitly_wait(0)` is set deliberately;
  every interaction goes through `WebDriverWait` in `base_page.py` so
  failures are clear about *which* element timed out, instead of a
  generic implicit-wait timeout with no context.
- **Locators use the site's `data-qa` attributes** (`data-qa="login-email"`,
  `data-qa="login-password"`, `data-qa="login-button"`) where available,
  since these are part of the site's own test-automation support and are
  more stable than CSS classes tied to styling.
- **Credentials are never hard-coded.** They're loaded from `.env` via
  `python-dotenv` so the repository stays safe to make public.
