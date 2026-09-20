##################### Hard Starting Project ######################

import pandas as pd
import datetime as dt
import random
import smtplib
from email.message import EmailMessage


my_email = "ch2267329@gmail.com"
my_password = "hcom mviu fbfn oiyl"


# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

data = pd.read_csv("birthdays.csv")


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches
# one of the keys in birthday_dict.

birthdays_dict = {}

for index, row in data.iterrows():
    birthdays_dict[(row["month"], row["day"])] = row


today = dt.datetime.now()

today_month = today.month
today_day = today.day


if (today_month, today_day) in birthdays_dict:

    birthday_person = birthdays_dict[(today_month, today_day)]


    # 3. If step 2 is true, pick a random letter from letter templates
    # and replace the [NAME] with the person's actual name from birthdays.csv

    letter_number = random.randint(1, 3)

    letter_file = f"letter_templates/letter_{letter_number}.txt"

    with open(letter_file) as file:
        letter_content = file.read()

    personalized_letter = letter_content.replace(
        "[NAME]",
        birthday_person["name"]
    )


    # 4. Send the letter generated in step 3
    # to that person's email address.

    receiver_email = birthday_person["email"]

    message = EmailMessage()

    message["Subject"] = "Happy Birthday!"
    message["From"] = my_email
    message["To"] = receiver_email

    message.set_content(personalized_letter)


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()

        connection.login(
            user=my_email,
            password=my_password
        )

        connection.send_message(message)


    print("Email sent!")