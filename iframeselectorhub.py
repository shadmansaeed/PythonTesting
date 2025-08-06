import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://selectorshub.com/iframe-scenario/")
time.sleep(2)

#iframe = driver.find_element(By.XPATH, "//iframe[@id='pact1']")
#driver.switch_to.frame(iframe)

#driver.find_element(By.XPATH, "//input[@id='inp_val']").send_keys("Shadman Saeed")
#time.sleep(3)
iframe1 = driver.find_element(By.XPATH, "//iframe[@id='pact1']")
driver.switch_to.frame(iframe1)

iframe2 = driver.find_element(By.XPATH, "//iframe[@id='pact2']")
driver.switch_to.frame(iframe2)

iframe3 = driver.find_element(By.XPATH, "//iframe[@id='pact3']")
driver.switch_to.frame(iframe3)

driver.find_element(By.XPATH, "//input[@id='glaf']").send_keys("Sabriah Saeed")
time.sleep(3)


