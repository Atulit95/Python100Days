import datetime as dt
import smtplib
import random

my_email = "atulitgupta57@gmail.com"
password = "miuvmsytawmhlman"

# ----------------------------- Quote Selection ---------------------#

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # print(weekday)
    with open(file="email_quotes.txt", mode="r") as quote:
        quote_list = quote.readlines()
        toaday_quote = random.choice(quote_list)
# ------------------------------- Email Section -----------------------#
# Used port 587 for SMTP with TLS encryption, which is the standard port for SMTP submission.
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="soulknight67@myyahoo.com",
        msg=f"Subject:Monday Motivation\n\n{toaday_quote}",  # '\n\n' sepaerate message from subject
    )
