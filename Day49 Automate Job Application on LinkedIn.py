#This program doesn't work if linkedin Captcha page shows up.
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def replace(path,text):
    '''This function replaces the text of input field'''
    #Note: For this to work the the input field must be filled with some previous recomended value.
    driver.find_element(By.XPATH,path).clear()
    driver.find_element(By.XPATH,path).send_keys(text)
    driver.find_element(By.XPATH,path).send_keys(Keys.ENTER)

def abort():
    '''Aborts the Application if criterion not met'''
    driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss").click()
    discard_button=driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Keep browser open after program finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# Create and configure the browser
driver=wd.Chrome(chrome_option)
driver.maximize_window() # opens window in maximised view.

#Opens linkedin Login page.
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

#Manages Login Credentials
driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]").click()# signIn button click
driver.find_element(By.ID,"username").send_keys("YOUR_EMAIL") #ENter your email
driver.find_element(By.ID,"password").send_keys("PASSWORD")  # Enter your password
driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button").click()# submit SignIn details

#Replaces Search bar for desired job.
replace(path='//*[@class="jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-box__text-input--with-clear jobs-search-global-typeahead__input"]',text="forntend developer")
replace(path='//*[@class="jobs-search-box__text-input jobs-search-box__text-input--with-clear"]',text="Worldwide")
time.sleep(5)

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for list in all_listings:
    list.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("9988776655")

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            abort()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        continue

    except NoSuchElementException:
        abort()
        print("No application button, skipped.")
        continue
#Ends the Session
driver.close()

