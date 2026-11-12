from bikes import Station, Bike

class Client:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bike = None

    def take_bike(self, station):
        self.bike = station.give_bike()
        if self.bike != "нічо":
            return None

    def calculate_price(ride_time, bike_type):
        price_per_minute = Bike.per_minute(bike_type)
        return price_per_minute * ride_time

    # def return_bike(station, bike_type, number):
