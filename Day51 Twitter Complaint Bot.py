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

# twitter login page
twitter_home_page = driver.get(url='https://x.com/home')

#delay and google login option
sleep(2)
login_option_select = driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div')
login_option_select.click()

# # windows list 
# windows_list = driver.window_handles

# #for login pag we get a new popup window so we have to switch window so that we can fill details to tha window
# login_window = driver.switch_to.window(windows_list[1])

# #login details
sleep(4)
username_element = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username_element.click()
username_element.send_keys("@knightSlays307")
next_button = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
next_button.click()

#security check bypass
sleep(2)
email_or_phone_element = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[1]/div/span')
if email_or_phone_element.text == "Phone or email":
    email_element = driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    email_element.send_keys('guptaatulit55@gmail.com')
    email_element.send_keys(Keys.ENTER)


sleep(2)# sleep because password element needed to be loaded before we can enter the paasword
password_element = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_element.click()
password_element.send_keys("998877@At")


login_button = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
login_button.click()
