# Importing necessary modules from Behave, Selenium, and page objects
from behave import given, when, then
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step: Open the browser and navigate to the Guvi login page
@given("the user is on the Guvi login page")
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.page = LoginPage(context.driver)
    context.page.navigate_login_page()

# Step: Open the browser and navigate to the Guvi login page
@when('the user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):
        context.page.enter_credentials(username, password)

# Step: Click the login button
@when('the user click login button')
def step_impl(context):
    context.page.click_login()

# Step: Verify login result based on expected outcome (success/failure)
@then('login should "{result}"')
def step_impl(context, result):
    if result == "success":
        assert context.page.is_dashboard_present, "Expected dashboard after login"
        context.driver.quit()
    else:
        assert context.page.is_login_failed(), "Expected error message"
        context.driver.quit()

# Step: Check if the username input field is visible
@then("the username input field should be visible")
def step_impl(context):
    assert context.page.is_username_visible(), "Username field not visible"
    context.driver.quit()

# Step: Check if the password input field is visible
@then("the password input field should be visible")
def step_impl(context):
    assert context.page.is_password_visible(), "Password field not visible"
    context.driver.quit()

# Step: Check if the login button is enabled
@then("the login button should be enabled")
def step_impl(context):
    assert context.page.is_login_button_enabled(), "Login button is enabled"
    context.driver.quit()

# Step: Log in using valid credentials for logout button test
@given("the user is logged in with valid credentials")
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.page = LoginPage(context.driver)
    context.page.navigate_login_page()
    context.page.enter_credentials("aniha2525@gmail.com", "Aniha@guvi123")
    context.page.click_login()
    context.page.close_popup()

# Step: Check if logout button is present and clickable
@then("the logout button should enabled")
def step_impl(context):
    assert context.page.is_logout_button_enabled(), "Logout button is clickable"
    context.driver.quit()