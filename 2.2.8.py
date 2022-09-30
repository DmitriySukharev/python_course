from re import X
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
input3.send_keys("mail@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')      
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

button = browser.find_element (By.XPATH,'/html/body/div/form/button')
button.click()