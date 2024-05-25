from selenium import webdriver as wd
from selenium.webdriver.common.by import By
chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=wd.Chrome(chrome_option)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_digits=driver.find_element(By.CLASS_NAME,value="a-price-whole")
decimal_value=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print(price_digits.text)
print(decimal_value)

driver.close() # it closes single instance of the browser
# driver.quit()  # It closes all instance of the browser