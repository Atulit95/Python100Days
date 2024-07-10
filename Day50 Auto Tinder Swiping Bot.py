from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Keep browser open after prograrm finishes
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

#list of window handles to switch between windows
windows_list=driver.window_handles

#Switching to second window or pop-up window
second_window=driver.switch_to.window(windows_list[1])

#delay and login detai submission
sleep(2)
email_detail = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_detail.send_keys("9555943149")

password_detail = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password_detail.send_keys("998877@At")

#this do the job of submitting detail and complete login process
password_detail.send_keys(Keys.ENTER)

sleep(2)
original_window=driver.switch_to.window(windows_list[0])
# give permission to pop-ups
sleep(6)
location_popup = driver.find_element(by=By.XPATH,value='//*[@id="u1146625330"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
location_popup.click()

sleep(2)
notification_popup = driver.find_element(by=By.XPATH,value='//*[@id="u1146625330"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div')
notification_popup.click()

sleep(1)
cookie_popup_accept = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
cookie_popup_accept.click()

sleep(5)
for i in range(1,10):
    driver.find_element(by=By.XPATH,value='//*[@id="u-1419960890"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()
    i+=1
    sleep(2)
