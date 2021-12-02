# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData

sheet_data = DataManager()
data = sheet_data.read_city_names()
flight_data = FlightData()
notification = NotificationManager()

# Find IATA for each cities and filled the info into the google sheet.
# for datum in data:
#     object_ID = datum['id']
#     city = datum['city']
#     x = flight_data.get_IATA_code(datum['city'])
#     price = datum['lowestPrice']
#     sheet_data.put(object_ID, city, x, price)

message = input("Please input the departure city name and the arrival city name separated by a comma: \n")

message = message.split(',')
message[0] = flight_data.get_IATA_code(message[0].title())
message[1] = flight_data.get_IATA_code(message[1].title())

cheapest_option = flight_data.get_ticket_data(message[0], message[1])

if cheapest_option != {}:
    notification.send_message(cheapest_option)
