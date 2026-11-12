class Bike:
    def __init__(
        self,
        number,
        bike_type,
    ):
        self.number = number
        self.bike_type = bike_type

    def per_minute(self):
        if self.bike_type == "звичайний":
            return 2
        elif self.bike_type == "електричний":
            return 5

    def is_usable(self):
        if self.bike_type == "звичайний" or self.bike_type == "електричний":
            return True


class Station:
    def __init__(self, name_station):
        self.name_station = name_station
        self.bikes = []

    def add_bike(self, bikes):
        self.bikes.append(bikes)

    def give_bike(self):
        if self.bikes:
            return self.bikes.pop()
        else:
            return None

    def count_bikes(self):
        return len(self.bikes)

    def __str__(self):
        return f"Станція {self.name_station} з {len(self.bikes)} велосипедами"
