from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from backend.database.databases import produtos

navegar = webdriver.Chrome()
navegar.get("https://www.pingodoce.pt/?")
time.sleep(3)

cokisEnter = navegar.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
cokisEnter.send_keys(Keys.ENTER)


for produto in produtos:
    print(produto)
    searchElente = navegar.find_element(By.ID, "header-search-bar")
    searchElente.clear()
    searchElente.send_keys(produto)
    searchElente.send_keys(Keys.ENTER)
    time.sleep(3)



navegar.close()