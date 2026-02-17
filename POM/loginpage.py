# import time
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class LoginPage:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#         self.wait = WebDriverWait(driver, 10)
#
#     def enter_email(self, email_id):
#         self.driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_password(self, password):
#         self.driver.find_element('id', 'Password').send_keys(password)
#
#     def click_on_login_btn(self):
#         self.driver.find_element('xpath', '//input[@value="Log in"]').click()
#         time.sleep(2)
#
#     def validate_unsucessfull_msg(self):
#         try:
#             self.wait.until(EC.visibility_of_element_located(('xpath', '//span[contains(text(), "Login was unsuccessful")]')))
#             print("Unsuccessfull login")
#         except:
#             print("Succesfull login")

######################################################################################################

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from object_repository.loginpage_locators import LoginPageLocators

log = LoginPageLocators()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver  ## self.driver --> driver = webdriver.Chrome()
        self.wait = WebDriverWait(driver, 10)

    def enter_email(self, email_id):
        self.driver.find_element(*log.email).send_keys(email_id)

    def enter_password(self, password):
        self.driver.find_element(*log.password).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element(*log.login_button).click()
        time.sleep(2)

    def validate_unsucessfull_msg(self):
        try:
            self.wait.until(EC.visibility_of_element_located(log.unsucessfull_msg))
            print("Unsuccessfull login")
        except:
            print("Succesfull login")














































































