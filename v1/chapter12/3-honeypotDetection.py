from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Edge(executable_path='v1/chapter10/msedgedriver.exe')
driver.get("http://pythonscraping.com/pages/itsatrap.html")
links = driver.find_elements(by=By.TAG_NAME, value="a")
for link in links:
    if not link.is_displayed():
        print("The link "+link.get_attribute("href")+" is a trap")

fields = driver.find_elements(by=By.TAG_NAME, value="input")
for field in fields:
    if not field.is_displayed():
        print("Do not change value of "+field.get_attribute("name"))