from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep

# Keeep browser open after prograrm finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# Create and configure browser
driver=wd.Chrome(chrome_option)
driver.maximize_window()

tinder_home_page = driver.get(url="https://tinder.com/")

# delay of 2 sec to load all the elements
sleep(2)

#clicks on create account button
Create_account = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
Create_account.click()

#delay and click on more option.
sleep(2)
more_option_element = driver.find_element(by=By.XPATH,value='//*[@id="u1146625330"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
if more_option_element.text=="MORE OPTIONS":
    more_option_element.click()

#delay and click on the facebook option
sleep(2)
facebook_element=driver.find_element(by=By.XPATH,value='//*[@id="u1146625330"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_element.click()

#delay and login detai submission
sleep(2)
email_detail = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_detail.send_keys("9555943149")
