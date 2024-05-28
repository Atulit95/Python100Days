from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def right_pannel_data():
    '''Checks for the each upgrade cost at runtime and returns the list of upgrade cost.'''
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

def run_for_5_seconds(): 
    start_time = time.time() 
    while True: 
        # Finds cookie & runs this line for 5 seconds
        driver.find_element(By.ID,"cookie").click()
        # when time runs out we move to right pannel get the max upgrade we can get 
        if time.time() - start_time >= 5:
            # finds amount of cookie present in the instance
            cookie_amount=int(driver.find_element(By.ID,"money").text.replace(",",""))
            # checks for each upgade value 
            list2=right_pannel_data()
            index=0
            for value in list2:
                # checks for the max value we can take for upgrade depending upon cookie amount
                if value<=cookie_amount:
                    index=list2.index(value)
                    # clicks on the max upgrade available
            driver.find_element(By.XPATH,f"//div[@id='store']/div[{index+1}]").click()
            run_for_5_seconds()

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# create and Configure the browser
driver=wd.Chrome(chrome_option)

# Navigate to game page
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

run_for_5_seconds()

driver.close()