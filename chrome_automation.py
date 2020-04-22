# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
#setting path for the chromedriver 
driver = webdriver.Chrome(executable_path='C:/Webderivers/chromedriver.exe')

#comadinging it to open kaggle
driver.get("https://www.kaggle.com");
#opening a new tab 
driver.execute_script("window.open('https://github.com','');")
 