import bikes
# import client
import random

station1 = bikes.Station("Station 1")
station2 = bikes.Station("Station 2")

bike1 = bikes.Bike("1", "звичайний")
bike2 = bikes.Bike("2", "звичайний")
bike3 = bikes.Bike("3", "звичайний")
bike4 = bikes.Bike("4", "звичайний")
bike5 = bikes.Bike("5", "електричний")
bike6 = bikes.Bike("6", "електричний")
bike7 = bikes.Bike("7", "електричний")
bike8 = bikes.Bike("8", "електричний")

station1.add_bike([bike1, bike2, bike7, bike8])
station2.add_bike([bike3, bike4, bike5, bike6])

# client1 = client.Client("Петро", 500)
# client2 = client.Client("Олена", 700)
