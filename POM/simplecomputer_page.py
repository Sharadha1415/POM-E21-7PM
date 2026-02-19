# import time
#
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# class SimpleComputerPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.ac = ActionChains(driver)
#
#     def click_on_processor(self):
#         self.driver.find_element('xpath', '//input[@id="product_attribute_75_5_31_96"]').click()
#         time.sleep(2)
#
#     def click_on_add_to_cart(self):
#         self.driver.find_element('xpath', '//input[@id="add-to-cart-button-75"]').click()
#         time.sleep(2)
#
#     def scroll_to_home(self):
#         self.ac.send_keys(Keys.HOME).perform()
#         time.sleep(1)
#
#     def click_on_shopping_cart(self):
#         self.driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
#         time.sleep(2)
#

# #########################################################################################################
#
# import time
#
# from object_repository.simplecomp_page_locators import SimpleComputerPageLocators
# from utilities.generic_utilities import WebDriverUtility
#
# simp = SimpleComputerPageLocators()
#
# class SimpleComputerPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.util = WebDriverUtility(driver)
#
#     def click_on_processor(self):
#         # self.driver.find_element(*simp.processor).click()
#         self.util.click_on_ele(simp.processor)
#         time.sleep(2)
#
#     def click_on_add_to_cart(self):
#         # self.driver.find_element(*simp.add_to_cart).click()
#         self.util.click_on_ele(simp.add_to_cart)
#         time.sleep(2)
#
#     def scroll_to_home(self):
#         # self.ac.send_keys(Keys.HOME).perform()
#         # time.sleep(1)
#         self.util.scroll_to_home()
#
#     def click_on_shopping_cart(self):
#         # self.driver.find_element(*simp.shopping_cart).click()
#         self.util.click_on_ele(simp.shopping_cart)
#         time.sleep(2)
#

#########################################################################################################

import time

from object_repository.simplecomp_page_locators import SimpleComputerPageLocators
from utilities.generic_utilities import WebDriverUtility

simp = SimpleComputerPageLocators()

class SimpleComputerPage:

    def __init__(self, driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)

    def click_on_processor(self):
        self.util.click_on_ele(simp.processor)
        time.sleep(2)

    def click_on_add_to_cart(self):
        self.util.click_on_ele(simp.add_to_cart)
        time.sleep(2)

    def scroll_to_home(self):
        self.util.scroll_to_home()

    def click_on_shopping_cart(self):
        self.util.click_on_ele(simp.shopping_cart)
        time.sleep(2)















