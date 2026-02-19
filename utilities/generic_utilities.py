import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class WebDriverUtility:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ac = ActionChains(driver)

    def click_on_ele(self, var_name):
        self.driver.find_element(*var_name).click()

    def enter_data(self, var_name, data):
        self.driver.find_element(*var_name).send_keys(data)

    def ele_visibility(self, ele):
        self.wait.until(EC.visibility_of_element_located(ele))

    def select_drpdwn_by_txt(self, var_name, text):
        listbox = self.driver.find_element(*var_name)
        select_obj = Select(listbox)
        select_obj.select_by_visible_text(text)
        time.sleep(1)

    def pgdn_scroll(self):
        self.ac.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    def hover(self, var_name):
        ele = self.driver.find_element(*var_name)
        self.ac.move_to_element(ele).perform()
        time.sleep(1)

    def scroll_to_home(self):
        self.ac.send_keys(Keys.HOME).perform()
        time.sleep(1)


















































































