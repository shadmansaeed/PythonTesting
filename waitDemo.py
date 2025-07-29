import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
name = "ber"
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys(name)
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # list
len(results)
#assert count  > 0
assert len(results) > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click() #chaining of web element
    #time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(8)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
#assert