import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.shop import ShopPage
from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    loginPage = LoginPage(driver)
    shop_page = loginPage.login("rahulshettyacademy", "learning")

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Blackberry")
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validating_order()

    time.sleep(3)
