import datetime as dt
import smtplib, random, os
from dotenv import load_dotenv

load_dotenv()

# Globals
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

# Open and read quotes
# quotes_file = open("quotes.txt", "r")
# quotes_list = [row for row in quotes_file]
# quotes_file.close()
with open("quotes.txt", "r") as file:
    quotes_list = file.readlines()
    random_quote = random.choice(quotes_list)
    print(random_quote)

# Check if current day is Monday and if so, send an email
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # connection = smtplib.SMTP("smtp.gmail.com", port=587)  # Port used by Gmail
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Encrypts the email in transit
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                             to_addrs=os.getenv("TO_EMAIL"),
                             msg=f"Subject:Weekly Quote\n\n{random_quote}"
                             )
