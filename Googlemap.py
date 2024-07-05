from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.google.com/maps/@10.5442763,76.1383668,7z')
sleep(2)


def serchplace():
    Place = driver.find_element(By.XPATH,'//*[@id="searchboxinput"]')
    Place.send_keys("Kochi")
    Submit = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    Submit.click()

serchplace()

def directions():
    try:
        directions = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'GgK1If'))
        )
        print(directions.text)
    finally:
        driver.close()

directions()
