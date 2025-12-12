from car import Car
from electric_car import ElectricCar

my_nissan = Car("Nissan", "Altima", 2021)
print(my_nissan.get_descriptive_name())
my_tesla = ElectricCar("Tesla", "ModelY", 2024)
print(my_tesla.get_descriptive_name())
