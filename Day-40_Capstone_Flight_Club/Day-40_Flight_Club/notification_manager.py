# =============================
# Notification Manager
# =============================

"""
This method is responsible for sending out notifications via SMS, WhatsApp or Email to registered users.
"""

# =============================
# Imports and Environment Variables
# =============================

import os
import smtplib
from email.message import EmailMessage
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv

load_dotenv()

# =============================
# NotificationManager Class
# =============================

class NotificationManager:
    def __init__(self):
        # Twilio Client
        self.client = Client(os.getenv('TWILIO_ACCOUNT_SID'),
                             os.getenv('TWILIO_AUTH_TOKEN')
                             )

        # SMTP Settings
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = os.getenv('SMTP_PORT', 465)
        self.smtp_username = os.getenv('SMTP_USERNAME')
        self.smtp_password = os.getenv('SMTP_PASSWORD')

        # Sender settings
        self.from_sms_number = os.getenv('TWILIO_VIRTUAL_NUMBER')
        self.from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
        self.from_email = os.getenv('SMTP_FROM_EMAIL')

        # Recipient Settings
        self.to_sms_number = os.getenv('MY_SMS_NUMBER')
        self.to_whatsapp_number = os.getenv('MY_WHATSAPP_NUMBER')
        #  self.to_email = os.getenv('SMTP_TO_EMAIL')


    def send_sms_notification(self, message):
        """
        Sends an SMS notification via Twilio.
        """
        try:
            message = self.client.messages.create(
                from_=self.from_sms_number,
                body=message,
                to=self.to_sms_number
            )

            print(message.sid)
        except TwilioRestException as e:
            print(f"❌ Failed to send SMS: {e}")

    def send_whatsapp_notification(self, message):
        """
        Sends a WhatsApp notification via Twilio.
        """
        try:
            message = self.client.messages.create(
              from_=self.from_whatsapp_number,
              body=message,
              to=self.to_whatsapp_number
            )

            print(message.sid)
        except TwilioRestException as e:
            print(f"❌ Failed to send WhatsApp message: {e}")

    def send_email_notification(self, to_email, message):
        """
        Sends an Email notification via SMTP.
        """
        # --- Control the subject line ---
        subject = "Flight Club Notification"

        # Building the Email message
        email_message = EmailMessage()
        email_message["Subject"] = subject
        email_message["From"] = self.from_email
        email_message["To"] = to_email
        email_message.set_content(message)

        try:
            print(f"Connecting to SMTP Server via SSL...")
            server = smtplib.SMTP_SSL(host=self.smtp_server, port=int(self.smtp_port))
            server.login(user=self.smtp_username, password=self.smtp_password)
            server.send_message(email_message)
            print(f"✅ Email sent to {to_email}")
            #  view_message = input(f"Do you want to view the message? (y/n): ").strip().lower()
            # if view_message == "y":
            #     print(f"{email_message}")

        except smtplib.SMTPException as e:
            print(f"❌ Failed to send Email: {e}")