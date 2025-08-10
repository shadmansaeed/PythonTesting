import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_options = webdriver.ChromeOptions

# if certificate error shows
chrome_options.add_argument("--ignore-certificate-errors")
# chrome driver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# javascript executor
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# screenshot
driver.get_screenshot_as_file("test.png")
time.sleep(2)
