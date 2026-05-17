import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
FROM_ADDRESS = os.getenv('FROM_ADDRESS')
TO_ADDRESS = os.getenv('TO_ADDRESS')
SMTP_SERVER = os.getenv('SMTP_SERVER')

def send_email(body):
    # --- Construct an Email Object ---
    msg = EmailMessage()
    msg['Subject'] = "Product Price Alert!"
    msg['From'] = FROM_ADDRESS
    msg['To'] = TO_ADDRESS
    msg.set_content(body)
    try:
        print("Sending email...")
        # Send message via SSL
        server = smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT)
        server.login(TO_ADDRESS, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent!")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")