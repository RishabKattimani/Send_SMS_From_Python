import os
from twilio.rest import Client

# Configurations
account_sid = "YOUR_ACCOUNT_SID_HERE"
auth_token = "YOUR_AUTH_TOKEN_HERE"

# Setting the client with the configurations
client = Client(account_sid, auth_token)

# Creating the message
client.messages.create(
    to="TO_NUMBERr",
    from_="FROM_NUMBER",
    body="This is a message send from Python"
)
