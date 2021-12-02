import requests
from flight_search import FlightSearch


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data_search = FlightSearch()

    def get_IATA_code(self, city):
        """
        returns the IATA code for the airport from the city inputted.
        """
        response = self.flight_data_search.search_IATA(city)['locations'][0]['id']
        return response

    def get_ticket_data(self, departure_city, arrival_city):
        """
        Scan through the flight data and get the cheapest one.
        :return: a dictionary that contains the ticket price, departure city, departure date,
        arrival city, arrival date, and ticket ordering link.
        """
        data = (self.flight_data_search.search_flight(departure_city, arrival_city))
        cheapest_price = data['data'][0]['price']
        index = 0
        cheapest_ticket_info = {}
        while index != (len(data['data']) - 1):
            if cheapest_price > data['data'][index + 1]['price']:
                cheapest_price = data['data'][index + 1]['price']
                cheapest_ticket_info = self.get_cheapest_ticket_info(data['data'][index + 1])
            elif cheapest_price == data['data'][index + 1]['price']:
                cheapest_ticket_info = self.get_cheapest_ticket_info(data['data'][index])
            index += 1

        return cheapest_ticket_info

    def get_cheapest_ticket_info(self, flight_data):

        data = {
            "price": flight_data['price'],
            "cityFrom": flight_data['cityFrom'],
            "local_departure": flight_data['local_departure'],
            "cityTo": flight_data['cityTo'],
            "utc_arrival": flight_data['utc_arrival'],
            "ticket_link" : flight_data['deep_link']
        }
        return data
