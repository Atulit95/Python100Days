from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# User Details 
EMAIL = "bijon89426@bsidesmn.com"
PASSWORD = "998877@At"
# Keep browser open after prograrm finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# Create and configure browser
driver=wd.Chrome(chrome_option)
driver.maximize_window()

# instagram login page
instagram_home_page = driver.get(url='https://www.instagram.com/')

# login_details
sleep(1)
user_email_element = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
user_email_element.click()
user_email_element.send_keys(EMAIL)

user_password = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
user_password.click()
user_password.send_keys(PASSWORD)
user_password.send_keys(Keys.ENTER)


# # In case of account suspension policy try executes.
# try:
#     sleep(2)
#     x = driver.find_element(by=By.CSS_SELECTOR,value='//span[contains(text(), "Dismiss")]')
#     if x.text == "Dismiss":
#         hoverable = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Q3"]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div')
#         ActionChains(driver)\
#             .move_to_element(hoverable)\
#             .click()
#         # x.click()
# except NoSuchElementException:

# #popup rejection
sleep(3)
first_popup_element = driver.find_element(by=By.CSS_SELECTOR,value='.x78zum5.xdt5ytf.x1e56ztr')
first_popup_element.click()

sleep(2)
second_popup_element = driver.find_element(by=By.CSS_SELECTOR,value='._a9_1')
second_popup_element.click()



amazing_food_images
