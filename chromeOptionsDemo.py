import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# Service diye path dite hobe
service = Service("C:\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
time.sleep(3)
driver.quit()

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

#driver.get("https://rahulshettyacademy.com/angularpractice/")

#print(driver.title)