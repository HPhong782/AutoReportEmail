from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from AutoReportEmail.Locators.emailLocators import EmailLocators
import time


class SendEmailPage():
    def __init__(self, driver):
        self.driver = driver

        self.send_email_button = EmailLocators.send_mess_button_xpath
        self.receiver_email = EmailLocators.email_reciver_xpath
        self.title_email = EmailLocators.email_title_xpath
        self.email = EmailLocators.message_xpath
        self.file_import = EmailLocators.file_import_xpath
        self.send_button = EmailLocators.send_button_xpath


    def send_email(self, receiver_email, title_email, email):
        driver = self.driver

        driver.find_element(By.XPATH,self.send_email_button).click()
        driver.find_element(By.XPATH,self.receiver_email).send_keys(receiver_email)
        driver.find_element(By.XPATH,self.title_email).send_keys(title_email)
        driver.find_element(By.XPATH,self.email).send_keys(email)
        driver.find_element(By.XPATH,self.file_import).click()
        time.sleep(15)
        driver.find_element(By.XPATH,self.send_button).click()
        time.sleep(15)