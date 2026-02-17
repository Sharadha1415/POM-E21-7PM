# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class HomePage:
#
#     def __init__(self, driver):
#         self.driver = driver            ## self.driver --> driver = webdriver.Chrome()
#         self.wait = WebDriverWait(driver, 10)
#         self.ac = ActionChains(driver)
#
#     def validate_homepage(self):
#         self.wait.until(EC.visibility_of_element_located(('xpath', '//img[@alt="Tricentis Demo Web Shop"]')))
#         time.sleep(1)
#
#     def click_on_login(self):
#         self.driver.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(1)
#
#     def validate_logout(self):
#         self.wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="Log out"]')))
#         time.sleep(2)
#
#     def hover_to_computers(self):
#         computers = self.driver.find_element('xpath', '//a[contains(text(), "Computers")]')
#         self.ac.move_to_element(computers).perform()
#         time.sleep(2)
#
#     def click_on_desktop(self):
#         self.driver.find_element('xpath', '//a[contains(text(), "Desktops")]').click()
#         time.sleep(2)

########################################################################################################

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from object_repository.homepage_locators import HomePageLocators

home = HomePageLocators()


class HomePage:

    def __init__(self, driver):
        self.driver = driver  ## self.driver --> driver = webdriver.Chrome()
        self.wait = WebDriverWait(driver, 10)
        self.ac = ActionChains(driver)

    def validate_homepage(self):
        self.wait.until(EC.visibility_of_element_located(home.logo))
        time.sleep(1)

    def click_on_login(self):
        self.driver.find_element(*home.login_link).click()
        time.sleep(1)

    def validate_logout(self):
        self.wait.until(EC.visibility_of_element_located(home.logout_link))
        time.sleep(2)

    def hover_to_computers(self):
        computers = self.driver.find_element(*home.computers_ele)
        self.ac.move_to_element(computers).perform()
        time.sleep(2)

    def click_on_desktop(self):
        self.driver.find_element(*home.desktops).click()
        time.sleep(2)



















































































