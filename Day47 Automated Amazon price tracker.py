import requests
from bs4 import BeautifulSoup
import lxml

response=requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
product_page=response.text
# print(product_page)

soup=BeautifulSoup(product_page,"lxml")
price=soup.select(selector=".za-price-whole")
print(price)
