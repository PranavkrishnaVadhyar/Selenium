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
        directions = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button'))
        )
        directions.click()

        sleep(10)

        start = driver.find_element(By.XPATH,'//*[@id="sb_ifc50"]/input')
        start.send_keys("Palarivattom")
        Submit = driver.find_element(By.XPATH, '//*[@id="directions-searchbox-0"]/button[1]')
        Submit.click()
        sleep(5)
    finally:
        driver.close()

directions()
