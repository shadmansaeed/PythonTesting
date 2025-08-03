import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform() #go to hover text

#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(3)