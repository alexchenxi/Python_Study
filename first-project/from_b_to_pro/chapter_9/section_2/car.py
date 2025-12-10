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


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.mile = 123
my_new_car.read_mile()
my_new_car.update_mile(888)
my_new_car.read_mile()
my_new_car.update_mile(555)

my_new_car_2 = Car("Nissan", "altima", 2022)
my_new_car_2.increment_mile(2000)
my_new_car_2.read_mile()
my_new_car_2.increment_mile(-2000)
