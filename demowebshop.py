# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait = WebDriverWait(driver, 10)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(1)
#
# wait.until(EC.visibility_of_element_located(('xpath', '//img[@alt="Tricentis Demo Web Shop"]')))
# time.sleep(1)
#
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# time.sleep(1)
# driver.find_element('id', 'Email').send_keys('abcdefgh@gmail.com')
# driver.find_element('id', 'Password').send_keys('abc@12345')
# driver.find_element('xpath', '//input[@value="Log in"]').click()
# time.sleep(2)
#
# try:
#     wait.until(EC.visibility_of_element_located(('xpath', '//span[contains(text(), "Login was unsuccessful")]')))
#     print("Unsuccessfull login")
# except:
#     print("Succesfull login")
#


####################################################################################################################

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait = WebDriverWait(driver, 10)
ac = ActionChains(driver)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(1)

wait.until(EC.visibility_of_element_located(('xpath', '//img[@alt="Tricentis Demo Web Shop"]')))
time.sleep(1)

driver.find_element('xpath', '//a[text()="Log in"]').click()
time.sleep(1)
driver.find_element('id', 'Email').send_keys('steve.jobs123@gmail.com')
driver.find_element('id', 'Password').send_keys('stevejobs')
driver.find_element('xpath', '//input[@value="Log in"]').click()
time.sleep(2)

wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="Log out"]')))
time.sleep(2)

computers = driver.find_element('xpath', '//a[contains(text(), "Computers")]')
ac.move_to_element(computers).perform()
time.sleep(2)

driver.find_element('xpath', '//a[contains(text(), "Desktops")]').click()
time.sleep(2)

sortby = driver.find_element('xpath', '//select[@id="products-orderby"]')
select_sortby = Select(sortby)
select_sortby.select_by_visible_text("Price: Low to High")
time.sleep(2)

viewas = driver.find_element('xpath', '//select[@id="products-viewmode"]')
select_viewas = Select(viewas)
select_viewas.select_by_visible_text("List")
time.sleep(2)

ac.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)

driver.find_element('xpath', '(//a[text()="Simple Computer"])[2]').click()
time.sleep(2)

driver.find_element('xpath', '//input[@id="product_attribute_75_5_31_96"]').click()
time.sleep(2)

driver.find_element('xpath', '//input[@id="add-to-cart-button-75"]').click()
time.sleep(2)

ac.send_keys(Keys.HOME).perform()
time.sleep(1)

driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
time.sleep(2)

country = driver.find_element('xpath', '//select[@id="CountryId"]')
select_country = Select(country)
select_country.select_by_visible_text("India")
time.sleep(1)

driver.find_element('xpath', '//input[@id="termsofservice"]').click()
time.sleep(1)

driver.find_element('xpath', '//button[@id="checkout"]').click()















































































































































































