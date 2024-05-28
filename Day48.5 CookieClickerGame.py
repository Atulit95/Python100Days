from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def right_pannel_data():
    list1=[]
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyCursor b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyGrandma b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyFactory b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyMine b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyShipment b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyAlchemy\ lab b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyPortal b").text.split()[-1].replace(",","")))
    list1.append(int(driver.find_element(By.CSS_SELECTOR,"#buyTime\ machine b").text.split()[-1].replace(",","")))
    return list1

def run_for_3_seconds(): 
    start_time = time.time() 
    while True: 
        # Perform some operations here 
        driver.find_element(By.ID,"cookie").click()
        # For demonstration purposes, we can just keep looping until 3 seconds have passed 
        if time.time() - start_time >= 5:
            cookie_amount=int(driver.find_element(By.ID,"money").text.replace(",","")) 
            list2=right_pannel_data()
            index=0
            for value in list2:
                if value<=cookie_amount:
                    index=list2.index(value)
                    # print(index)
            driver.find_element(By.XPATH,f"//div[@id='store']/div[{index+1}]").click()
            run_for_3_seconds()

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# create and Configure the browser
driver=wd.Chrome(chrome_option)

# Navigate to game page
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

run_for_3_seconds()

driver.close()