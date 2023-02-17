# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json
import requests
import time

while True:
        key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        data = requests.get(key)
        data = data.json()
        Btcprice=(f"{data['symbol']} price is {data['price']}")

        # Set environment variables for your credentials
        # Read more at http://twil.io/secure
        account_sid = "ACb50d6d5364f65f22c40d5a03d3f24322"
        auth_token = "7a2acb7972baef9ad22ba0e93b03afba"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body=Btcprice,
        from_="+13159798914",
        to="+919994240600"
        )

        print("The message sent :", message.sid)
        time.sleep(10)