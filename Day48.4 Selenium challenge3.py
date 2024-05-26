from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# create and Configure the browser
driver=wd.Chrome(chrome_option)

# Navigate to fake registration page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the first name,last name, email
first_name=driver.find_element(By.NAME,"fName")
last_name=driver.find_element(By.NAME,"lName")
email=driver.find_element(By.NAME,"email")

# Fill out yhe form
first_name.send_keys("knight")
last_name.send_keys("Slays")
email.send_keys("knight@slays")

# locate the signup button and click it.
submit=driver.find_element(By.CSS_SELECTOR,".btn")
submit.click()

driver.close