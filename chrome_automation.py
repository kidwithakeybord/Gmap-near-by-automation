# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from selenium import webdriver
#setting path for the chromedriver 
driver = webdriver.Chrome(executable_path='C:/Webderivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
#comadinging it to open kaggle
driver.get("https://www.kaggle.com");
driver.implicitly_wait(10)
#opening a new tab 
driver.execute_script("window.open('https://github.com','');")
 
