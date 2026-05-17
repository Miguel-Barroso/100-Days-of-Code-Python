# Automatic Birthday Wisher (Email)

import datetime as dt
import pandas, random, smtplib, os
from dotenv import load_dotenv

load_dotenv()

# Global variables
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

# Getting the current date and time
now = dt.datetime.now()
today = (now.month, now.day)
# print(today)

# Importing birthday data
birthday_data_frame = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data_frame.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    print(f"It's {birthdays_dict[today]['name']}'s birthday!")

    # Chooses a random letter, replaces the [NAME] placeholder
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter_template:
        letter = letter_template.read()
        letter = letter.replace("[NAME],", birthdays_dict[today]["name"])
        print(letter)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Encrypts the email in transit
        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[today][1],
                            # Works but deprecated. Should access the key "email" instead!
                            msg=f"Subject:Happy Birthday!\n\n{letter}"
                            )

else:
    print("It's no one's birthday...")
