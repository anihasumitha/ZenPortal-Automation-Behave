#Locators for login page
from selenium.webdriver.common.by import By

class Locators:
    username_field = (By.XPATH, '//input[@placeholder="Enter your mail"]')
    password_field = (By.XPATH, '//input[@placeholder="Enter your password "]')
    login_button = (By.XPATH, '//button[@class="primary-btn sign-in-pad"]')
    dashboard = (By.XPATH, '//p[contains(text(),"Dashboard")]')
    error_message = (By.XPATH, '//p[contains(text(),"*Incorrect mail or password!")]')
    dropdown=(By.XPATH,'//div[@class="profile-click-icon-div"]')
    logout_button = (By.XPATH,"//div[contains(text(),'Log out')]")
    close_popup_button = (By.XPATH,'//button[@class="custom-close-button"]')
