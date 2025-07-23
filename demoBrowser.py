import time
from selenium import webdriver
# chrome driver service
driver = webdriver.Edge()
driver.get("https://202.51.185.99/")
driver.find_element()
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(4)