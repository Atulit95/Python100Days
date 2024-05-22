import requests
from bs4 import BeautifulSoup
import smtplib

DESIRED_PRICE=40.05
URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

my_email = "sender_email"
password = "your_email_password"


response=requests.get(url=URL)
product_page=response.text
# print(product_page)

soup=BeautifulSoup(product_page,"lxml")
price=soup.find(class_="a-offscreen").getText()
price=float(price.split("$")[1])

if price>DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="reciever_email",
            msg=f"""Subject:sent mail\n\n The product you are looking for has now got a lower price than your desired price.\n 
            Make sure to check that out.Click below to view the product.\n
            {URL}
            """,  # '\n\n' sepaerate message from subject
        )