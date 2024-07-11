from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from speedTest import speedTest
from time import sleep

#UP and Down Speed array from speedtest.net
speed_list=speedTest()

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
try:
    email_or_phone_element = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[1]/div/span')
    if email_or_phone_element.text == "Phone or email":
        email_element = driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        email_element.send_keys('guptaatulit55@gmail.com')
        email_element.send_keys(Keys.ENTER)
    sleep(2)# sleep because password element needed to be loaded before we can enter the paasword
    password_element = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_element.click()
    password_element.send_keys("998877@At")

except NoSuchElementException:
    sleep(2)# sleep because password element needed to be loaded before we can enter the paasword
    password_element = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_element.click()
    password_element.send_keys("998877@At")


login_button = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
login_button.click()

#Welcome message close
sleep(4)
welecome_popup_x_element = driver.find_element(by= By.XPATH,value='//*[@id="layers"]/div/div[1]/div/div/div/button')
welecome_popup_x_element.click()

post_button = driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
post_button.click()

sleep(1)
post_text = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
post_text.send_keys(f'Hey Internet Provider, why is my Internet speed {speed_list[0]}down/{speed_list[1]}up when I pay for 150down/10up')

#final post submission
sleep(1)
final_post_buton = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
final_post_buton.click()

#closes the browser
driver.quit()

