import requests
from twilio.rest import Client
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ.get('account_sID')
        self.auth_token = os.environ.get('auth_token')
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, data):
        """
        send a text message to specified phone number
        """
        message = self.client.messages \
            .create(
            body=f"Hi there, I have found you the ticket you were looking to {data['cityTo']} for {data['price']}, "
                 f"the departure time is {data['local_departure']} and the arrival time is {data['utc_arrival']}, the link to buy the ticket is {data['ticket_link']}",
            from_=os.environ.get('test_number'),
            to=os.environ.get('my_number')
        )
