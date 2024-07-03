from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#sample commit
query = 'laptop'
driver.get(f"https://www.amazon.com/s?k={query}&crid=3FCLG8QYEJEX9&sprefix=laptop%2Caps%2C403&ref=nb_sb_noss_1")
element = driver.find_element(By.CLASS_NAME,"puisg-col-inner")
print(element.text)