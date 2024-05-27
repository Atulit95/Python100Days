from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# create and Configure the browser
driver=wd.Chrome(chrome_option)

# Navigate to game page
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

# find and click on cookie
count=15
while count!=0:
    driver.find_element(By.ID,"cookie").click()
    # cookie_amount=driver.find_element(By.ID,"money").value_of_css_property(By.CSS_SELECTOR,".grayed")
    # print(cookie_amount.text)
    # time.sleep(3)
    count-=1
# cookie_amount=driver.find_element(By.ID,"money")

hello

cursor_redeem_value=driver.find_element(By.CSS_SELECTOR,"#buyCursor b").text.split()[-1]
print(cursor_redeem_value)




# driver.close()