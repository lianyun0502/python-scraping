from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.youdao.com")
driver.find_element(by=By.ID, value="query").send_keys('hello')#提交輸入框的內容
driver.find_element(by=By.ID, value="query").submit()
driver.quit()