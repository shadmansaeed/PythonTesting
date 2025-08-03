import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

# chrome driver service
name = "ber"
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys(name)
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # list
len(results)
#assert count  > 0
assert len(results) > 0

for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click() #chaining of web element
    #time.sleep(1)
assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
Sum = 0
for price in prices:
    Sum = Sum + int(price.text)

print(Sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert Sum == totalAmount

# insert promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(8)
wait = WebDriverWait(driver, 10)  # explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text) # print promoinfo

discountedAmount= int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)  #display discounted amount
#assert