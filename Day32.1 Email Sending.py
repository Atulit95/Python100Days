import smtplib

my_email = "your_email"
password = "your_password"

# Used port 587 for SMTP with TLS encryption, which is the standard port for SMTP submission.
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="reciever's email",
        msg="Subject:sent mail\n\nHello",  # '\n\n' sepaerate message from subject
    )
