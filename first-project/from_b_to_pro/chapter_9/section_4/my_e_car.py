from car import ElectricCar as EC

my_e_car = EC("Tesla", "modelY", 2025)
print(my_e_car.get_descriptive_name())
my_e_car.battery.describe_battery()
my_e_car.battery.get_range()
