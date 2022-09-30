from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://swiftbook.org/users/sign_in"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "user_email")
    input1.send_keys("sukharevdmitrii1@gmail.com")
    input2 = browser.find_element(By.ID, "user_password")
    input2.send_keys("123456")
    button = browser.find_element(By.NAME, "commit")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

