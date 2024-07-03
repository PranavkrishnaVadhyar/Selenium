from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.environ['PATH'] += r"C:/Users/bpran/Desktop/selenium/Selenium/chromedriver_win32/chromedriver.exe"
#Chrome version : 126.0.6478.127  chrome://version
#
driver = webdriver.Chrome()

'''
driver.get('https://the-internet.herokuapp.com/dropdown')
driver.implicitly_wait(3)  # wait for 3 secs

my_element = driver.find_element(By.ID,'dropdown')
my_element.click()
'''

# enter keyword to search
keyword = "geeksforgeeks"
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/find_element_by_id-driver-method-selenium-python/")
 
# get element 
element = driver.find_element(By.ID ,"openInApp-modal")
 
# print complete element


if (element):
    print("found")