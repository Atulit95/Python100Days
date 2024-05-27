from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# create and Configure the browser
driver=wd.Chrome(chrome_option)

# Navigate to game page
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

# find and click on cookie
count=1
# while count!=0:
driver.find_element(By.ID,"cookie").click()

# driver.close()