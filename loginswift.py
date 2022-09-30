import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://swiftbook.org/users/sign_in")
time.sleep(3)
driver.get("https://swiftbook.org/courses")
time.sleep(3)
driver.quit()