from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r'"C:\Users\bhanu\Desktop\chromedriver.exe"')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.spotify.com/in-en/signup')



# ID , Xpath , CSSselectors , Classanme, name , linkTest
driver.find_element(By.NAME, "email").send_keys('hello@123')
driver.find_element(By.ID,"password").send_keys('heloo@123')
driver.find_element(By.CLASS_NAME,"bNNEyC").click()

# for Xpath ==//tagname[@attribute = 'value']
driver.find_element(By.XPATH,"//div[@data-encore-id='formGroup']").click()
# for CSS tagname[attribute = 'value']
driver.find_element(By.CSS_SELECTOR, 'input[name="displayname"]').send_keys('Bhanu')
# print(massege)
# driver.find_element(By.NAME,"email").send_keys('heloo@122')

# driver.find_element(By.XPATH,"//input[@name='password']").send_keys('Password')
# driver.find_element(By.XPATH,"//input[@checked='checked']").click()
# /html/body/div[1]/main/div/div/form/div[6]