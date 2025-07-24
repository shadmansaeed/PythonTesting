import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
name = "shadman saeed"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText) #display text of alert
time.sleep(1)
assert name in alertText # make sure shadman name is exist in alert box
alert.accept()  #click ok from pop-up
time.sleep(2)
#alert.dismiss() #click cancel from pop-up