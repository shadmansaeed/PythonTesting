import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()


windowsOpen = driver.window_handles

driver.switch_to.window(windowsOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(5)