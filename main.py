from fastapi import FastAPI
from twilio.rest import Client
import time
from threading import Thread

app = FastAPI()

# Your Twilio account SID and auth token
account_sid = "your_id"
auth_token = "you_token"
client = Client(account_sid, auth_token)

# The phone numbers to send the SMS to
phone_numbers = ["+91xxxxxxxxx"]

# Fire station phone number
fire_station_number = "+91xxxxxxxxxx"


def send_sms():
    for number in phone_numbers:
        message = client.messages.create(
            body=f"Fire detected! Please contact the nearest fire station: {nearest_firestation}",
            from_="+xxxxxxxxxxxxxx",
            to=number,
        )
        print(message.sid)
    time.sleep(30)
    message = client.messages.create(
        body="Fire detected at location. Please act immediately.",
        from_="+xxxxxxxxxxxxxx",
        to=fire_station_number,
    )
    print(message.sid)


@app.get("/detected")
def detected():
    # Start a new thread to send the SMS messages
    Thread(target=send_sms).start()
    return {"status": "messages being sent"}
