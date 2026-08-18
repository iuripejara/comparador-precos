from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from backend.database.databases import produtos

navegar = webdriver.Chrome()
navegar.get("https://www.auchan.pt/")
time.sleep(15)

cokisEnter = navegar.find_element(By.ID,"onetrust-accept-btn-handler" )
cokisEnter.send_keys(Keys.ENTER)


for produto in produtos:
    print(produto)
    searchElente = navegar.find_element(By.ID, "search-suggestions-input")
    searchElente.clear()
    searchElente.send_keys(produto)
    searchElente.send_keys(Keys.ENTER)
    time.sleep(3)



navegar.quit()