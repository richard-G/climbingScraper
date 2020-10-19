from twilio.rest import Client
import os

# twilio config
account_sid = os.environ['twilio-sid']
auth_token = os.environ['twilio-token']
client = Client(account_sid, auth_token)


def send_text(body):
    message = client.messages.create(
        to="+447411411435",
        from_="+14048009173",
        body=body)


def construct_message(availabilities):
    body = 'update: \n'
    # construct message body
    for day, value in availabilities.items():
        if value != 'AvailabilityFull.':
            body += f'\navailability at slot: {day}. ({value})\n'
        else:
            body += f'\nno availability at slot: {day}. ({value})\n'

    send_text(body)
