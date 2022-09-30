from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x_element = x_element1.get_attribute("valuex")
    x = x_element
    y = calc(x)
    
    
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    time.sleep(1)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    time.sleep(1)
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()