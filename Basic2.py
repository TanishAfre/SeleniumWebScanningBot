import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://syntaxprojects.com/basic-first-form-demo.php")
sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

driver.implicitly_wait(10)

sum1.send_keys(Keys.NUMPAD5, )
sum2.send_keys(6)

btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()
