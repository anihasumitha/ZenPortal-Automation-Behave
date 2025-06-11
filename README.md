# ZenPortal-Automation-Behave

This project automates login functionality testing for the Guvi Zen portal using Python, Selenium, and Behave.

## What it does

- Checks visibility of username and password fields
- Verifies login button state
- Validates successful and failed login attempts
- Confirms logout option appears after login

Tools used

- Python
- Selenium WebDriver
- Behave (BDD framework)
- Page Object Model design

## How to run

1. Install dependencies with `pip install -r requirements.txt`
2. Run tests using `behave --no-capture`

## Folder overview

- `features/` – test scenarios and step definitions
- `pages/` – page classes for Selenium actions
- `locators/` – web element locators

