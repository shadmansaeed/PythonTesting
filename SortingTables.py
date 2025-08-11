import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_options = webdriver.ChromeOptions

# chromedriver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
# collect all vegetable name --> browser sorted vegitable list
# sort this vegetablelist == newSortedList