from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from AutoReportEmail.Pages.loginEmailPage import LoginPage
from AutoReportEmail.Pages.sendEmailPage import SendEmailPage


class LoginTest(unittest.TestCase):

    #Setup browers
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_email(self):
        driver = self.driver
        self.driver.get("https://gmail.com")

        #login
        login_email = LoginPage(driver)
        login_email.enter_username("<your email>")
        login_email.enter_password("<your password>")
        login_email.click_login()

        #Send_email
        send_email = SendEmailPage(driver)
        send_email.send_email("<name reciever'semail>","<Your Title>","<Your messages>")     

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()