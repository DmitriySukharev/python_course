from selenium import webdriver
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element1 = browser.find_element(By.ID, 'num1')
    x = int(str(x_element1.text))

    x_element2 = browser.find_element(By.ID, 'num2')
    y = int(str(x_element2.text))
    
    def calc(x,y): 
        return str(x+y)

    z = calc(x,y)

    select = Select(browser.find_element(By.CSS_SELECTOR, "[ID='dropdown']"))
    select.select_by_value(str(z))
    
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()