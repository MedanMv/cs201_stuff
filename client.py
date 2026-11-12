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

    def calculate_price(self, ride_time):
        price_per_minute = self.bike.per_minute()
        return price_per_minute * ride_time

    def return_bike(self, station):
        station.add_bike(self.bike)
        self.bike = None

    def __str__(self):
        return f"Клієнт {self.name} з балансом {self.balance} грн"
