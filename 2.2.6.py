from re import X
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = " https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    x_element1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = str(x_element1.text)
    y = calc(x)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()