import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.read_end_point = os.environ.get('sheety_read_end_point')
        self.put_end_point = os.environ.get('sheety_put_end_point')
        self.token_username = os.environ.get('authentication_token_username')
        self.token_password = os.environ.get('authentication_token_password')
        self.authorization_token = os.environ.get('authorization_header_token')
        self.headers = {
            'Username': self.token_username,
            'Password': self.token_password,
            'Authorization': self.authorization_token
        }

    def read_city_names(self):
        """
        read a piece of data from the google sheets using sheety api
        """

        response = requests.get(url=self.read_end_point, headers=self.headers)

        return response.json()

    def put(self, object_ID, city, code, price):
        """
        Write or update a piece of data from the google sheets using sheety api
        """

        keys = {
            'price': {
                'city': city,
                'iataCode': code,
                'lowestPrice': price}
        }

        response = requests.put(url=f"{self.put_end_point}{object_ID}", headers=self.headers, json=keys)
        return response.text