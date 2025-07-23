import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
# work with more than 1 element
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))  # to know the length

# To click element with text
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)

# print(driver.find_element(By.ID, "autosuggest").text)  #this will use when website reload the hardcoded text

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))  # when value dynamically update through script then this works
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "bbIndia"