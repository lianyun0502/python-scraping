from selenium import webdriver
import time

#REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
# driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')
driver = webdriver.Edge(executable_path='v1/chapter10/msedgedriver.exe')
#driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5)
print(driver.find_element(value="content").text)
driver.close()