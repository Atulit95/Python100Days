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
    # Scrapping data from zillow using Beautifulsoup
    address_text = listing.find("address").getText()
    address_list.append((address_text[2:].strip(" "))[0:-1])
    price_text = listing.find(
        "span", class_="PropertyCardWrapper__StyledPriceLine"
    ).getText()
    price_list.append(price_text[0:6])
    url_text = listing.find("a", class_="property-card-link").get("href")
    url_list.append(url_text)
# print(address_list)

# Part 2 Filling google form using selenium

chrome_option = wd.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = wd.Chrome(chrome_option)
driver.maximize_window()

for i in range(0, len(address_list)):
    google_form_page = driver.get(url="your_google_form_link")
    # fills details to address field
    address_field = driver.find_element(
        by=By.XPATH,
        value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    sleep(2)
    address_field.click()
    address_field.send_keys(address_list[i])
    
    # fills details to price field
    price_field = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    sleep(2)
    price_field.click()
    price_field.send_keys(price_list[i])
    
    # fills details to url field
    url_field = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    sleep(2)
    url_field.click()
    url_field.send_keys(url_list[i])
    
    submit_button = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

driver.quit()
