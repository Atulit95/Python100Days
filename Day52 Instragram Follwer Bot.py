from selenium import webdriver as wd

# Keep browser open after prograrm finishes
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# Create and configure browser
driver=wd.Chrome(chrome_option)
driver.maximize_window()

# instagram login page
instagram_home_page = driver.get(url='https://www.instagram.com/')