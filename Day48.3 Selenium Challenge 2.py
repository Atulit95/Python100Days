from selenium import webdriver as wd
from selenium.webdriver.common.by import By

chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=wd.Chrome(chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(article_count.text)
driver.close()
