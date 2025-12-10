# 9.1
class Restaurant:
    def __init__(self, resteraurant_name, cuisine_type):
        self.resteraurant_name = resteraurant_name
        self.cuisine_type = cuisine_type

    def describe_resteraurant(self):
        print(
            f"The name of this resteraurant is {self.resteraurant_name}, its cuisine type is {self.cuisine_type}"
        )

    def open_resteraurant(self):
        print(f"{self.resteraurant_name.title()} is now opening!")


restaurant = Restaurant("Burger King", "fastfood")
print(restaurant.resteraurant_name)
print(restaurant.cuisine_type)
restaurant.describe_resteraurant()
restaurant.open_resteraurant()

print("################################")


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(
            f"{self.first_name.title()} {self.last_name.title()} is a {self.age} years old user."
        )

    def greet_user(self):
        print(f"Hello {self.first_name.title()}!")


alex = User("alex", "zhang", 36)
bob = User("bob", "boy", 31)
alex.describe_user()
alex.greet_user()
print(alex.last_name)
