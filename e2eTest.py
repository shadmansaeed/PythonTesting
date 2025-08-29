import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(@href,'shop)]'     a[href*='shop']

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

products= driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName= product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":



time.sleep(5)