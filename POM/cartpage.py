import time

# from selenium.webdriver.support.select import Select
#
# class CartPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def select_country(self, country_name):
#         country = self.driver.find_element('xpath', '//select[@id="CountryId"]')
#         select_country = Select(country)
#         select_country.select_by_visible_text(country_name)
#         time.sleep(1)
#
#     def click_terms_conditions(self):
#         self.driver.find_element('xpath', '//input[@id="termsofservice"]').click()
#         time.sleep(1)
#
#     def click_on_checkout(self):
#         self.driver.find_element('xpath', '//button[@id="checkout"]').click()

#####################################################################################################

import time

from selenium.webdriver.support.select import Select
from object_repository.cartpage_locators import CartPageLocators

cart = CartPageLocators()

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def select_country(self, country_name):
        country = self.driver.find_element(*cart.country_loc)
        select_country = Select(country)
        select_country.select_by_visible_text(country_name)
        time.sleep(1)

    def click_terms_conditions(self):
        self.driver.find_element(*cart.terms_service).click()
        time.sleep(1)

    def click_on_checkout(self):
        self.driver.find_element(*cart.checkout).click()



















































