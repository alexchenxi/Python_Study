# 9.6
class Restaurant:
    def __init__(self, resteraurant_name, cuisine_type):
        self.resteraurant_name = resteraurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resteraurant(self):
        print(
            f"The name of this resteraurant is {self.resteraurant_name}, its cuisine type is {self.cuisine_type}"
        )

    def open_resteraurant(self):
        print(f"{self.resteraurant_name.title()} is now opening!")

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print(
                f"Warning, you cannot set number served lesser than its current number!"
            )

    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print(f"Warning, you cannot add a negative number!")


class IceCreamStand(Restaurant):
    def __init__(self, resteraurant_name):
        super().__init__(resteraurant_name, "Icecream")
        self.flavors = ["Strawberry", "Vinilla", "Chocolate"]

    def describe_flavors(self):
        print(
            f"This resteraunt {self.resteraurant_name} has {self.cuisine_type} favors:"
        )
        for flavor in self.flavors:

            print(f"-{flavor}")


dq = IceCreamStand("Dairy Queen")
dq.describe_flavors()

print("#######################")

# 9.7 9.8


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"{self.first_name.title()} {self.last_name.title()} is a {self.age} years old user."
        )

    def greet_user(self):
        print(f"Hello {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Priviliges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def showPrivileges(self):
        print(f"Admin role has following previliges:")
        for p in self.privileges:
            print(f"- {p}")


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Priviliges()


admin_one = Admin("Admin", "Trump", 99)
admin_one.privileges.showPrivileges()


print("#########################")


# 9.9
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

    def upgrade_battery(self):
        if self.battery_size != 65:
            print("Battery upgrade complete!")
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar("BYD", "Han", 2025)
my_car.battery.getRange()
my_car.battery.upgrade_battery()
my_car.battery.getRange()
