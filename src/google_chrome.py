from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://google.com")
time.sleep(2)
driver.quit()