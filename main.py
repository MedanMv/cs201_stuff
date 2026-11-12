import bikes
import client
import random
def main():
    profit = 0

    station1 = bikes.Station("Station 1")
    station2 = bikes.Station("Station 2")
    station3 = bikes.Station("Station 3")

    bike1 = bikes.Bike("1", "звичайний")
    bike2 = bikes.Bike("2", "звичайний")
    bike3 = bikes.Bike("3", "звичайний")
    bike4 = bikes.Bike("4", "звичайний")
    bike5 = bikes.Bike("5", "електричний")
    bike6 = bikes.Bike("6", "електричний")
    bike7 = bikes.Bike("7", "електричний")
    bike8 = bikes.Bike("8", "електричний")

    station1.add_bike(bike1)
    station1.add_bike(bike2)
    station1.add_bike(bike7)
    station1.add_bike(bike8)
    station2.add_bike(bike3)
    station2.add_bike(bike4)
    station2.add_bike(bike5)
    station2.add_bike(bike6)

    client1 = client.Client("Петро", 2000)
    client2 = client.Client("Олена", 3000)

    print(client1)
    print(station1)
    print(station2)
    print(station3)
    print()
    client1.take_bike(station1)
    mins_ride1 = random.randint(1, 60)
    try:
        trip1 = client1.bike.per_minute() * mins_ride1
        client1.return_bike(station2)
        client1.balance -= trip1
        profit += trip1
        print(client1)
        print(station1)
        print(station2)
        print(station3)
    except AttributeError:
        print("Vidsutni velosipedi")
        trip1 = 0
    print()
    client1.take_bike(station2)
    mins_ride1 = random.randint(1, 60)
    try:
        trip1 = client1.bike.per_minute() * mins_ride1
        client1.return_bike(station1)
        client1.balance -= trip1
        profit += trip1
        print(client1)
        print(station1)
        print(station2)
        print(station3)
    except AttributeError:
        print("Vidsutni velosipedi")
        trip1 = 0
    print()
    client1.take_bike(station1)
    mins_ride1 = random.randint(1, 60)
    try:
        trip1 = client1.bike.per_minute() * mins_ride1
        client1.return_bike(station2)
        client1.balance -= trip1
        profit += trip1
        print(client1)
        print(station1)
        print(station2)
        print(station3)
    
    except AttributeError:
        print("Vidsutni velosipedi")
        trip1 = 0
    print()

    print(client2)
    client2.take_bike(station3)
    mins_ride2 = random.randint(1, 60)
    try:
        print(station3)
        trip2 = client2.bike.per_minute() * mins_ride2
        client2.return_bike(station3)
        client2.balance -= trip2
        profit += trip2
        print(client2)
        print(station3)
    except AttributeError:
        print("Vidsutni velosipedi")
        trip2 = 0

    print(f"Profit = {profit} грн")
if __name__ == "__main__":
    main()
