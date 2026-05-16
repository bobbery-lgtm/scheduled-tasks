##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
from random import choice
import pandas
import os

# Email details for the "from" account
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# List of possible letter templates
letter_list = ("letter_1.txt", "letter_2.txt", "letter_3.txt")

# Get today's date
now = dt.datetime.now()
day_today = now.day
month_today = now.month

# Turn bday.csv into dict
data = pandas.read_csv("birthdays.csv")
bday_dict = data.to_dict(orient="records")

# Check bday month/day against today's month/day
for person in bday_dict:
    if person["month"] == month_today:
        if person["day"] == day_today:

            # Create bday email and insert name in randomly selected letter template
            with open(f"./letter_templates/{choice(letter_list)}") as letter_file:
                contents = letter_file.read()
                contents = contents.replace("[NAME]", person["name"])

                with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                    connection.starttls()
                    connection.login(my_email, password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=person["email"],
                        msg=f"Subject:Happy Birthday, {person["name"]}!\n\n{contents}"
                )
