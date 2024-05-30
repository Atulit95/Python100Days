from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def replace(path,text):
    "This function replaces the text of input field"
    #Note: For this to work the the input field must be filled with some previous recomended value.
    driver.find_element(By.XPATH,path).clear()
    driver.find_element(By.XPATH,path).send_keys(text)
    driver.find_element(By.XPATH,path).send_keys(Keys.ENTER)

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# create and Configure the browser
driver=wd.Chrome(chrome_option)
driver.maximize_window() # opens window in maximised view.

#Opens linkedin Login page.
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

#Manages Login Credentials
driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]").click()
driver.find_element(By.ID,"username").send_keys("gojay78158@jahsec.com")
driver.find_element(By.ID,"password").send_keys("998877@At")
driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button").click()

#Replaces Search bar for desired job.
replace(path='//*[@class="jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-box__text-input--with-clear jobs-search-global-typeahead__input"]',text="marketing intern app brewery")
replace(path='//*[@class="jobs-search-box__text-input jobs-search-box__text-input--with-clear"]',text="Worldwide")

#Fill details and Submit Your Application to the Company.
driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button').click()
driver.find_element(By.XPATH,'//*[@class=" artdeco-text-input--input"]').send_keys("7975647987")
driver.find_element(By.XPATH,'//*[@class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()

#Ends the Session
driver.close()

