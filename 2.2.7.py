from re import X
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')      
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)