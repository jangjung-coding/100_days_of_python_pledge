# twilio API : This is a python script to send SMS using twilio API

import requests
from twilio.rest import Client

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+17083040184',
  body='Hello from JJ',
  to='+18777804236'
)

print(message.sid)