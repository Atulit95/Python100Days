import datetime as dt
import pandas
import random
import smtplib

my_email = "atulitgupta57@gmail.com"
password = "miuvmsytawmhlman"
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)

# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in birthday_data.iterrows()
}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if today in birthday_dict:
    bithday_person = birthday_dict[today]
    file_path = f"letter_templates/text_{random.randint(1,3)}.txt"
    with open(file=file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", bithday_person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bithday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}",  # '\n\n' sepaerate message from subject
        )
