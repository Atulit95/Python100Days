from selenium import webdriver as wd
from selenium.webdriver.common.by import By

chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=wd.Chrome(chrome_option)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]").click()
driver.find_element(By.ID,"username").send_keys("soulknight67@myyahoo.com")
driver.find_element(By.ID,"password").send_keys("998877@At")
driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button").click()
driver.find_element(By.XPATH,'//*[@id="global-nav-search"]/div/div[2]/div[1]').send_keys("marketing")
# driver.find_element(By.XPATH,"//*[@id='global-nav']/div/nav/ul/li[3]/a/div/div/li-icon/svg").click()
# driver.close()