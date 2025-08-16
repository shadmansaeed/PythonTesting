import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
browserSortedVeggies = []
chrome_options = webdriver.ChromeOptions

# chromedriver service
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

time.sleep(2)
# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()


# collect all vegetable name --> browser sorted vege table list
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

# To make copy of a list
originalBrowserSortedList = browserSortedVeggies.copy()

# sort this BrowserSortedveggielis => newSortedList -->(A,B,C)
browserSortedVeggies.sort()

# sort this vegetablelist == newSortedList

assert browserSortedVeggies == originalBrowserSortedList

time.sleep(3)