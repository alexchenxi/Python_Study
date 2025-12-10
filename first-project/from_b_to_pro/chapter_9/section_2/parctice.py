# 9.4
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


restaurant = Restaurant("Burger King", "fastfood")
print(
    f"Resteraurant {restaurant.resteraurant_name} has served {restaurant.number_served} persons"
)
restaurant.number_served = 123
print(
    f"Resteraurant {restaurant.resteraurant_name} has served {restaurant.number_served} persons"
)


restaurant.set_number_served(150)
print(
    f"Resteraurant {restaurant.resteraurant_name} has served {restaurant.number_served} persons"
)
restaurant.set_number_served(120)

restaurant.increment_number_served(-1)
restaurant.increment_number_served(50)
print(
    f"Resteraurant {restaurant.resteraurant_name} has served {restaurant.number_served} persons"
)

print("################################")


# 9.5
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


alex = User("alex", "zhang", 36)
for item in range(1, 6):
    alex.increment_login_attempts()
print(alex.login_attempts)
alex.reset_login_attempts()
print(alex.login_attempts)
