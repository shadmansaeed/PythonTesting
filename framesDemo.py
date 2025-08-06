import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
time.sleep(8)

#driver.find_element(By.ID, "tinymce").clear()
#time.sleep(2)
#driver.find_element(By.ID, "tinymce").send_keys("This is iframe testing")


# Send Ctrl+A to select all and replace text
#driver.find_element(By.ID, "tinymce").send_keys(u'\ue009' + "a")  # u'\ue009' is Ctrl key
#time.sleep(3)

# Now locate the <body> tag, not by ID
editor = driver.find_element(By.TAG_NAME, "body")
time.sleep(2)
editor.clear()  # optional, may not always work
time.sleep(2)
editor.send_keys("This is iframe testing")

time.sleep(3)