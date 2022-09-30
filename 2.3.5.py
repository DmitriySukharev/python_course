from re import X
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import math 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
time.sleep(2)
browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
time.sleep(2)
button = browser.find_element (By.CSS_SELECTOR,'[class="btn btn-primary"]')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

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