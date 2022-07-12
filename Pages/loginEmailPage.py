from selenium import webdriver
from selenium.webdriver.common.by import By
from AutoReportEmail.Locators.emailLocators import EmailLocators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = EmailLocators.username_text_xpath
        self.password_textbox = EmailLocators.password_name_text
        self.button_next = EmailLocators.username_button_next_xpath
        self.login_button = EmailLocators.login_button_xpath
    
    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox).clear()
        self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)
        self.driver.find_element(By.XPATH, self.button_next).click()

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox).clear()
        self.driver.find_element(By.NAME, self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()