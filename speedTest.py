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

def speedTest():
    '''Return Array with two elements. First element being Download speed while other os Upload speed.'''
    # Speedtest Home page
    speed_test_homepage = driver.get(url='https://www.speedtest.net/')

    #Accepts privacy notification
    sleep(2)
    privacy_accept = driver.find_element(by=By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
    privacy_accept.click()

    # Go button click
    go_button = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    go_button.click()


    sleep(50) # requires time to calculate both speeds
    down_speed = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    up_speed =   driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    #Closes the browser
    driver.quit()

    return [down_speed, up_speed]
