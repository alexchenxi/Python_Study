class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mile = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_mile(self):
        print(f"This car has {self.mile} miles on it")

    def update_mile(self, mile):
        if mile >= self.mile:
            print(f"This car's mile has been updated!")
            self.mile = mile
        else:
            print(f"Warning, You can not set mile lesser than its actual mile run!")

    def increment_mile(self, mile):
        if mile > 0:
            self.mile += mile
        else:
            print(f"Warning, You cannot add a negatvie mile number!")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def getRange(self):
        print(f"This car can go about {self.battery_size*4} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(100)


my_e_car = ElectricCar("Tesla", "ModelY", 2024)
print(my_e_car.get_descriptive_name())
my_e_car.battery.describe_battery()
my_e_car.battery.getRange()
