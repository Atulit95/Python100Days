import smtplib

my_email = "atulitgupta57@gmail.com"
password = "miuvmsytawmhlman"

# Used port 587 for SMTP with TLS encryption, which is the standard port for SMTP submission.
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="soulknight67@myyahoo.com",
        msg="Subject:sent mail\n\nHello",  # '\n\n' sepaerate message from subject
    )
