import config
import smtplib
from email.mime.text import MIMEText

smtp_server = config.os.getenv("SMTP_SERVER")
smtp_port = config.os.getenv("SMTP_PORT")
smtp_username = config.os.getenv("SMTP_USERNAME")
smtp_password = config.os.getenv("SMTP_PASSWORD")
from_email = config.os.getenv("SMTP_FROM_EMAIL")
to_email = config.os.getenv("SMTP_TO_EMAIL")

def send_message(stock_news_message):
    try:
        # Builds the email message content
        subject = "Stock News Update"
        email_message = MIMEText(stock_news_message, "plain")
        email_message["Subject"] = subject
        email_message["From"] = from_email
        email_message["To"] = to_email

        # Connect to SMTP server
        server = smtplib.SMTP_SSL(smtp_server, int(smtp_port))
        server.login(smtp_username, smtp_password)

        # Send email
        server.sendmail(from_email, to_email, email_message.as_string())
        server.quit()

        print("Message sent!")
        view_message = input(f"Do you want to view the message? (yes/no):　").strip().lower()
        if view_message:
            print(f"Subject: {subject}\n{stock_news_message}")

    except Exception as err:
        print(f" Failed to send email: {err}")
