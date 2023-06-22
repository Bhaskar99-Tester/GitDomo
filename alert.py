from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service(r'"C:\Users\bhanu\Desktop\chromedriver.exe"')

driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
name = "bhanu lohani"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
#  to click on ok or yes  button on pop up
alert.accept()
#  to click on ccancle button

# alert.dismiss()