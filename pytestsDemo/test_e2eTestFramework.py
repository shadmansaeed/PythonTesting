import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.shop import ShopPage
from pageObjects.login import LoginPage

# json work
test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)  # load will convert json file into python object
    test_list = test_data["data"]


@pytest.mark.smoke # pytest -m smoke (when this use in terminal, then only run this test)
@pytest.mark.parametrize("test_list_item", test_list)  # this is used after json integration
def test_e2e(browserInstance, test_list_item):  # json
    driver = browserInstance

    # this line is in conftest "driver.get("https://rahulshettyacademy.com/loginpagePractise/")"

    loginPage = LoginPage(driver)
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart(test_list_item["productName"])  # json
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validating_order()

    time.sleep(3)
