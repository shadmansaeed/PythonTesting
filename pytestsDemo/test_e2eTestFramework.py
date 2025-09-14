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
    loginPage.login()

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Blackberry")
    shop_page.goToCart()


    # //a[contains(@href,'shop)]'     a[href*='shop']

    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    driver.find_element(By.ID, "country").send_keys('ind')

    # explicit wait

    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()

    # click on checkbox
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    # click purchase to submit
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # grab success text
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text

    # To check message
    assert "Success! Thank you!" in successText

    time.sleep(5)
