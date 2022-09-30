from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 
import time 
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button = browser.find_element (By.ID, "book" )
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
    
input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
input1.send_keys(y)

button = browser.find_element (By.XPATH,'/html/body/form/div/div/button')
button.click()

time.sleep(4)
browser.quit()
