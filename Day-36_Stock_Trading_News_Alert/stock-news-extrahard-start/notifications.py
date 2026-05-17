import config
from twilio.rest import Client
from_number = config.os.getenv("TWILIO_PHONE_NUMBER")
to_number = config.os.getenv("MY_PHONE_NUMBER")
account_sid = config.os.getenv("TWILIO_ACCOUNT_ID")
auth_token = config.os.getenv("TWILIO_API_KEY")
client = Client(account_sid, auth_token)

def send_message(stock_news_message):
    text_message = client.messages.create(
        body=f"{stock_news_message}",
        from_=f"{from_number}",
        to=f"{to_number}",
    )
    print(f"Will send this message:\n{stock_news_message}")
    message_status = client.messages(text_message.sid).fetch()
    print(f"Message status: {message_status.status}")
    print(f"Error message: {message_status.error_message}")
