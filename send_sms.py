from twilio.rest import Client
import os

# twilio config
# account_sid = 'AC97ff662869325707dcbc249e2c3865ad'
account_sid = os.environ['twilio-sid']
auth_token = os.environ['twilio-token']
# auth_token = '4720dbaac3bf65a0f8bcaf253dba579c'
client = Client(account_sid, auth_token)


def send_text(body):
    message = client.messages.create(
        to="+447411411435",
        from_="+14048009173",
        body=body)


