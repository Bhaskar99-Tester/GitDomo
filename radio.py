from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r'"C:\Users\bhanu\Desktop\chromedriver.exe"')

driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# for moving object best method to use//


# radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
# for radio in radios:
#     if radio.get_attribute('value')=='radio2':
#         radio.click()
#         assert radio.is_selected()
#         break

# if u know the option will not move than u can use direct method to call the code


radiobutton = driver.find_elements(By.CSS_SELECTOR,'.radioButton')
radiobutton[2].click()
assert radiobutton[2].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()