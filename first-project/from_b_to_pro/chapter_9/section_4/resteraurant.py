class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"The name of this restaurant is {self.restaurant_name}, its cuisine type is {self.cuisine_type}"
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now opening!")

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
