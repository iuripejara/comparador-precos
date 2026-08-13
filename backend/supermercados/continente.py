from selenium import webdriver
from selenium.webdriver.common.by import By
import time



navegar = webdriver.Chrome()
navegar.get("https://www.continente.pt/")

time.sleep(3)
title = navegar.title


textNAmeCategory = navegar.find_element("class name", "col-12.textbox-container").text
print(textNAmeCategory)
navegar.quit() 
