import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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
        product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
#checkout
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys('ind')

#explicit wait

wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

time.sleep(4)
# click on checkbox
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

# click purchase to submit
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

# grab success text
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

# To check message
assert "Success! Thank you!" in successText

time.sleep(5)