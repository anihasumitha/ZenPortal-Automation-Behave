# Required Selenium imports for waiting on elements and handling timeouts

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.web_locators import Locators

# Page Object Model for the Guvi login page
class LoginPage:

    # Constructor to initialize the driver and wait time
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    # Navigates to the Guvi login page
    def navigate_login_page(self):
        self.driver.get("https://v2.zenclass.in/login")

    # Fills in the username and password fields
    def enter_credentials(self, username, password):
        self.wait.until(EC.visibility_of_element_located(Locators.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(Locators.password_field)).send_keys(password)

    # Clicks the login button
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(Locators.login_button)).click()

    # Closes any popup that appears after login
    def close_popup(self):
        self.wait.until(EC.element_to_be_clickable(Locators.close_popup_button)).click()

    # Checks if the username input field is visible
    def is_username_visible(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.username_field)).is_displayed()
            return True
        except TimeoutException:
            return False

    # Checks if the password input field is visible
    def is_password_visible(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.password_field)).is_displayed()
            return True
        except TimeoutException:
            return False

    # Checks if the login button is enabled
    def is_login_button_enabled(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.login_button)).is_enabled()
            return True
        except TimeoutException:
            return False

    # Checks if the logout button is enabled after expanding dropdown
    def is_logout_button_enabled(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.dropdown)).click()
            self.wait.until(EC.presence_of_element_located(Locators.logout_button)).is_enabled()
            return True
        except TimeoutException:
            return False

    # Verifies if the dashboard is present after a successful login
    def is_dashboard_present(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.dashboard))
            return True
        except TimeoutException:
            return False

    # Detects if login failed based on error message visibility
    def is_login_failed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.error_message))
            return True
        except TimeoutException:
            return False