from selenium import webdriver as wd

chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=wd.Chrome(chrome_option)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

driver.close() # it closes single instance of the browser
driver.quit()  # IT closes all instance of the browser