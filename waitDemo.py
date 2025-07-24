import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
name = "ber"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys(name)
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
len(results)
#assert count  > 0
assert len(results) > 0

#assert