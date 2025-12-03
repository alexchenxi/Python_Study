class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


dog = Dog("Teddy", 3)
print(f"My dog's name is {dog.name}.")
print(f"My dog is {dog.age} years old.")
dog.sit()
dog.roll_over()
