import os
from dotenv import load_dotenv
load_dotenv()

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

import datetime as dt

now = dt.datetime.now()  # Getting the current date and time as an object
today = (now.month, now.day)  # Today tuple
# print(today)

import pandas
birthday_data_frame = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(row["month"], row["day"]):(row["name"], row["email"], row["year"], row["month"], row["day"]) for (index, row) in birthday_data_frame.iterrows()}  # chatGPT suggestion
# birthdays_dict = {(data_row.month or data_row["month"], data_row.day or data_row["day"]): data_row for (index, data_row) in birthday_data_frame.iterrows()}  # Angela's solution
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data_frame.iterrows()}  # Dict comprehension I chose
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()} --> iterating over every row
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthday_dict = {
#     (birthday_month, birthday_year): data_row
# }
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

import smtplib, random

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    print(f"It's {birthday_person['name']}'s birthday!")

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_template:
        letter = letter_template.read().replace("[NAME]", birthday_person["name"])
        print(letter)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Encrypts the email in transit
        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter}"
                            )

else:
    print("It's no one's birthday...")

