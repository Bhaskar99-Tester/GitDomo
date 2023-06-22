import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r'"C:\Users\bhanu\Desktop\chromedriver.exe"')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
checkboxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
     if checkbox.get_attribute('value')=='option2':
         checkbox.click()
         assert checkbox.is_selected()
         break

time.sleep(5)
