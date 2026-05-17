import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# SMTP Settings
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT', 465)
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')
smtp_to_email = os.getenv('SMTP_TO_EMAIL')
smtp_from_email = os.getenv('SMTP_FROM_EMAIL')

def send_email_notification(name, email, phone, message):
    """
    Sends an Email notification via SMTP.
    """

    # Building the Email message
    email_message = EmailMessage()
    email_message["Subject"] = "Contact Form"
    email_message["From"] = smtp_from_email
    email_message["To"] = smtp_to_email
    email_message["Reply-To"] = email
    content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    email_message.set_content(content)

    try:
        print(f"Connecting to SMTP Server via SSL...")
        server = smtplib.SMTP_SSL(host=smtp_server, port=int(smtp_port))
        server.login(user=smtp_username, password=smtp_password)
        server.send_message(email_message)
        print(f"✅ Email sent to {smtp_to_email}")
        print(f"{email_message}")

    except smtplib.SMTPException as e:
        print(f"❌ Failed to send Email: {e}")