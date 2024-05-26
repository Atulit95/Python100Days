from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha

#>> The code below get stuck at Captcha page of amazon.

chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=wd.Chrome(chrome_option)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

#>> To bypass captcha of amazon page we gonna use the following code.
# Use library AmazonCaptcha
link=driver.find_element(By.XPATH,"//div[@class='a-row a-text-center']//img").get_attribute("src")
captcha=AmazonCaptcha.fromlink(link)
solution=captcha.solve()
captcha_input=driver.find_element(By.ID,"captchacharacters").send_keys(solution)
captcha_submit=driver.find_element(By.CLASS_NAME,"a-button-text").click()

#>> After solution we can get details we want.

price_digits=driver.find_element(By.CLASS_NAME,value="a-price-whole").text
decimal_value=driver.find_element(By.CLASS_NAME,value="a-price-fraction").text
print(f"The price of desired product is {price_digits}.{decimal_value}")


# driver.close() # it closes single instance of the browser
# driver.quit()  # It closes all instance of the browser