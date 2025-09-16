from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):

        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        return
