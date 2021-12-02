import requests
from os import environ
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_end_point = environ.get('end_point')
        self.search_end_point = environ.get('search_by_query_end_point')
        self.api_key = environ.get('API_KEY')
        self.search_location_api = environ.get('search_by_query_apikey')
        self.tomorrow = (datetime.today() + relativedelta(day=1)).date().strftime('%d/%m/%Y')
        self.six_month_from_now = (datetime.today() + relativedelta(months=6)).date().strftime('%d/%m/%Y')

    def search_IATA(self, city):
        """
        searches for information about the city inputted.
        """
        headers = {
            "apikey": self.search_location_api
        }
        parameters = {
            'term': city,
            'locale': 'en-US',
            'location_types': 'airport',
            'limit': 1,
            'active_only': True
        }

        response = requests.get(url=self.search_end_point, headers=headers, params=parameters).json()
        return response

    def search_flight(self, city, city_to):
        """
        Searches flights that meets conditions suches departing location, arriving location, etc.
        """
        headers = {
            "apikey": self.api_key
        }
        parameters = {
            "fly_from": city,
            'fly_to': city_to,
            "date_from": self.tomorrow,
            "date_to": self.six_month_from_now,
            'max_stopovers': 5,
            'limit': 200
        }

        response = requests.get(url=self.api_end_point, headers=headers, params=parameters)
        return response.json()
