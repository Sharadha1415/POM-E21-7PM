import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(1)
    yield driver
    driver.close()

## setup --> driver = webdriver.Chrome(opts)