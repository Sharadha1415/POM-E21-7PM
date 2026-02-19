# import time
#
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# class DesktopPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.ac = ActionChains(driver)
#
#     def selecting_sortby(self, sort_ele):
#         sortby = self.driver.find_element('xpath', '//select[@id="products-orderby"]')
#         select_sortby = Select(sortby)
#         select_sortby.select_by_visible_text(sort_ele)
#         time.sleep(2)
#
#     def selecting_view(self, view_ele):
#         viewas = self.driver.find_element('xpath', '//select[@id="products-viewmode"]')
#         select_viewas = Select(viewas)
#         select_viewas.select_by_visible_text(view_ele)
#         time.sleep(2)
#
#     def scroll_pagedown(self):
#         self.ac.send_keys(Keys.PAGE_DOWN).perform()
#         time.sleep(1)
#
#     def click_on_simp_computer(self):
#         self.driver.find_element('xpath', '(//a[text()="Simple Computer"])[2]').click()
#         time.sleep(2)

# ###########################################################################################################
#
# import time
#
# from object_repository.desktoppage_locators import DesktopPageLocators
# from utilities.generic_utilities import WebDriverUtility
#
# desktop = DesktopPageLocators()
#
# class DesktopPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.util = WebDriverUtility(driver)
#
#     def selecting_sortby(self, sort_ele):
#         # sortby = self.driver.find_element(*desktop.sort)
#         # select_sortby = Select(sortby)
#         # select_sortby.select_by_visible_text(sort_ele)
#         # time.sleep(2)
#         self.util.select_drpdwn_by_txt(desktop.sort, sort_ele)
#
#     def selecting_view(self, view_ele):
#         # viewas = self.driver.find_element(*desktop.view)
#         # select_viewas = Select(viewas)
#         # select_viewas.select_by_visible_text(view_ele)
#         # time.sleep(2)
#         self.util.select_drpdwn_by_txt(desktop.view, view_ele)
#
#     def scroll_pagedown(self):
#         # self.ac.send_keys(Keys.PAGE_DOWN).perform()
#         # time.sleep(1)
#         self.util.pgdn_scroll()
#
#     def click_on_simp_computer(self):
#         # self.driver.find_element(*desktop.simp_comp).click()
#         self.util.click_on_ele(desktop.simp_comp)
#         time.sleep(2)

###########################################################################################################

import time

from object_repository.desktoppage_locators import DesktopPageLocators
from utilities.generic_utilities import WebDriverUtility

desktop = DesktopPageLocators()

class DesktopPage:

    def __init__(self, driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)

    def selecting_sortby(self, sort_ele):
        self.util.select_drpdwn_by_txt(desktop.sort, sort_ele)

    def selecting_view(self, view_ele):
        self.util.select_drpdwn_by_txt(desktop.view, view_ele)

    def scroll_pagedown(self):
        self.util.pgdn_scroll()

    def click_on_simp_computer(self):
        self.util.click_on_ele(desktop.simp_comp)
        time.sleep(2)















































