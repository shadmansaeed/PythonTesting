import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("jibonrootnext@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("shadman")   # CSS tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.ID, "exampleCheck1").click()

# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
# dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()  # xpath //tagname[@attribute='value']
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Urmi")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(3)