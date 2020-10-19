from twilio.rest import Client

# twilio config
account_sid = 'AC97ff662869325707dcbc249e2c3865ad'
auth_token = '4720dbaac3bf65a0f8bcaf253dba579c'
client = Client(account_sid, auth_token)


def send_text(body):
    message = client.messages.create(
        to="+447411411435",
        from_="+14048009173",
        body=body)


