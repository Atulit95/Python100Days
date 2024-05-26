#>> Our goal is to create nesteed dictionary as shown below from "pyhon.org" for "upcomming event"
# {0: {'time': '05-27-2024', 'event': 'Python 3.13.0 beta 1 released'}, 
#  1: {'time': '05-29-2024', 'event': 'PSF Grants Program 2022 & 2023 Transparency Report'}, 
#  2: {'time': '05-29-2024', 'event': 'PSF Board Election Dates for 2024'}, 
#  3: {'time': '06-01-2024', 'event': 'PSF Board Election Dates for 2024'}, 
#  4: {'time': '06-01-2024', 'event': "The PSF's 2023 Annual Impact Report is here!"}}

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

chrome_option=wd.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=wd.Chrome(chrome_option)
driver.get("https://www.python.org/")

dict={}
list1=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
i=0
for li in list1:
    dict[i]={"time":f"{li.text}-2024",
             "event":f"{driver.find_element(By.XPATH,f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{1+i}]/a").text}"}
    i+=1
    
print(dict)

driver.close()
