class Person:
    def __init__(self, name="Rose", favourite_food="pizza"):
        self.name = name
        self.favourite_food = favourite_food

    def get_food(self):
        print(f"{self.name}'s favourite food is {self.favourite_food}.")


p1 = Person("Jackson", "Hot-Dog")
# p1.name = "Rose"
# p1.favourite_food = "Pizza"
p1.get_food()

p2 = Person(favourite_food="Dumpling", name="Wayne")
p2.get_food()
