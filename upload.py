import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID, "downloadButton").click()

# edit the with uploaded file

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys("")


