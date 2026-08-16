from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



navegar = webdriver.Chrome()
navegar.get("https://www.continente.pt/")




cokisEnter = navegar.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
time.sleep(5)
cokisEnter.send_keys(Keys.ENTER)

searchElente = navegar.find_element(By.CLASS_NAME, "form-control.search-field.pwc-form-input.pwc-search-input")
searchElente.send_keys("arroz")
searchElente.send_keys(Keys.ENTER)
time.sleep(3)
navegar.quit() 
