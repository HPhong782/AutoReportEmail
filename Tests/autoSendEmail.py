from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from AutoReportEmail.Pages.loginEmailPage import LoginPage
from AutoReportEmail.Pages.sendEmailPage import SendEmailPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/phong.le/Desktop/Python_selenium/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_email(self):
        driver = self.driver
        self.driver.get("https://gmail.com")

        #login
        login_email = LoginPage(driver)
        login_email.enter_username("phong.le@terralogic.com")
        login_email.enter_password("phong78201330")
        login_email.click_login()

        #Send_email
        send_email = SendEmailPage(driver)
        send_email.send_email("phong.lephong@hcmut.edu.vn","Hello I am done","Xin chào mọi người, tạm biệt nhé!")
        # send_email = SendEmailPage(driver)
        # send_email.send_email_button()
        # send_email.receiver_email("phong.lephong@hcmut.edu.vn")
        # send_email.title_email("Hello I am done")
        # send_email.email("Xin chào mọi người, tạm biệt nhé!")
        # send_email.file_import()
        # time.sleep(15)
        # send_email.send_button()
        # time.sleep(15)       

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()