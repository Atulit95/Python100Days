from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

# Keeep browser open after prograrm finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# Create and configure browser
driver=wd.Chrome(chrome_option)
driver.maximize_window()

driver.get(url="https://tinder.com/")
time.sleep(2)
x=driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button').click()

