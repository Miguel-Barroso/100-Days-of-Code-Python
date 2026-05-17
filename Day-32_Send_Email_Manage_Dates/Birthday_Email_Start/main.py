# import smtplib
#
# my_email = "YOUR_EMAIL"
# my_password = "YOUR_APP_PASSWORD"
#
# #  connection = smtplib.SMTP("smtp.gmail.com", port=587)  # Port used by Gmail
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # Encrypts the email in transit
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="RECIPIENT_EMAIL",
#                         msg="Subject:Hello\n\nThis is the body of my email"
#                         )
# #  connection.close()  # Needed unless with keyword is used
#


# import datetime as dt
#
# now = dt.datetime.now()  # From the dt module, datetime class, use the method now() to get the current date and time
# # as an object
# print(now)
# year = now.year  # Accessing the year attribute from the now object
# print(year)
# month = now.month
# print(month)
# weekday = now.weekday()  # Calling the weekday() method returns a number 0-6
# print(weekday)
#
# # Specifying our own datetime object
# date_of_birth = dt.datetime(year=2018, month=5, day=5, hour=21, minute=21)
# print(date_of_birth)