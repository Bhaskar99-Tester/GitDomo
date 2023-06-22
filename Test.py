from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("bhanu\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH,"//div/input[@name='name']").send_keys("Bhaskar")
driver.find_element(By.XPATH,"//div/input[@name='email']").send_keys("bhanulohnai19992gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("bhanu@123")
driver.find_element(By.ID,"exampleCheck1").click()
dropdowm = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdowm.select_by_visible_text("Male")
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
msg =  driver.find_element(By.CSS_SELECTOR,".alert-success").text

assert "Success!" in msg
