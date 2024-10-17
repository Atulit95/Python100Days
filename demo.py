from time import sleep
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

chrome_option = wd.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = wd.Chrome(chrome_option)
driver.maximize_window()

google_form_page = driver.get(url="https://forms.gle/m8sBcyzPYtpE2kVm8")
# sleep(2)

address_field = driver.find_element(
    by=By.CSS_SELECTOR,
    value='#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input',
)
sleep(2)
# for i in range(0, len(address_list)):
address_field.click()
address_field.send_keys("vcfg")

driver.quit()