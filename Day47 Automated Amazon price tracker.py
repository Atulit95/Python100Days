import requests
from bs4 import BeautifulSoup
import lxml

response=requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
product_page=response.text
# print(product_page)

soup=BeautifulSoup(product_page,"lxml")
price=soup.select(selector=".a-price-whole")
print(price)
