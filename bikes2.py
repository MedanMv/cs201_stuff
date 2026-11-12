class Bike:
    def __init__(self, number, bike_type, charge=100):
        self.number = number
        self.bike_type = bike_type
        self.charge = charge

    def per_minute(self):
        if self.bike_type == "звичайний":
            return 2
        elif self.bike_type == "електричний":
            return 5

    def is_usable(self):
        if self.bike_type == "електричний":
            return self.charge >= 20
        return True


class Station:
    def __init__(self, name_station):
        self.name_station = name_station
        self.bikes = []

    def add_bike(self, bikes):
        self.bikes.extend(bikes)

    def give_bike(self):
        for bike in self.bikes:
            if bike.is_usable():
                self.bikes.remove(bike)
                return bike
        return None

    def count_bikes(self):
        return len(self.bikes)

    def __str__(self):
        return f"Станція {self.name_station} з {len(self.bikes)} велосипедами"


def low_charge_bikes(stations):
    result = []
    for station in stations:
        for bike in station.bikes:
            if bike.bike_type == "електричний" and bike.charge < 20:
                result.append((bike.number, station.name_station, bike.charge))
    return result
