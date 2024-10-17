from bs4 import BeautifulSoup
import requests
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep

# Finding and making list of all listing matching the criterion for user.

zillow_response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text

soup = BeautifulSoup(zillow_response, "html.parser")

listings = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

address_list = []
price_list = []
url_list = []

for listing in listings:
    address_text = listing.find("address").getText()
    address_list.append((address_text[2:].strip(" "))[0:-1])
    price_text = listing.find(
        "span", class_="PropertyCardWrapper__StyledPriceLine"
    ).getText()
    price_list.append(price_text[0:6])
    url_text = listing.find("a", class_="property-card-link").get("href")
    url_list.append(url_text)
# print(address_list)

# Part 2 Fillinhg form using selenium

chrome_option = wd.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = wd.Chrome(chrome_option)
driver.maximize_window()

google_form_page = driver.get(url="https://forms.gle/m8sBcyzPYtpE2kVm8")
# sleep(2)

address_field = driver.find_element(
    by=By.CLASS_NAME,
    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
)
# for i in range(0, len(address_list)):
address_field.click()
address_field.send_keys("vcfg")

driver.quit()
