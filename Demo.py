from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# --Chrome
# service_obj =Service(r'C:\Users\bhanu\Desktop\chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)

# --Edge
service_obj =Service(r'C:\Users\bhanu\Downloads\edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get('https://pypi.org/project/selenium/')

print(driver.title)
print(driver.current_url)
driver.get('https://pypi.org/help/')
driver.back()
driver.refresh()

driver.close()