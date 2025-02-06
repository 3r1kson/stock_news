from twilio.rest import Client

from config.config import get_twillio_sid, get_twillio_messaging_sid, get_twillio_token

account_sid = get_twillio_sid()
auth_token = get_twillio_token()
messaging_id = get_twillio_messaging_sid()

def send_sms(message):
    if not all([account_sid, auth_token, messaging_id]):
        print("Error: One or more credentials are missing.")
        return

    client = Client(str(account_sid), str(auth_token))

    message = client.messages.create(
      messaging_service_sid=str(messaging_id),
      body=message,
      to='+5541988500364'
    )
    print(message.status)