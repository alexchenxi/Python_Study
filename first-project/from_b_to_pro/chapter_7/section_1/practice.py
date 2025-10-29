# 7.1
car = input('Please type us what brand of car you want to rent?')
print(f"Let me see if I can find you a {car}")

# 7.2
dinning_number = input("Please input how many persons do you have?")
dinning_number = int(dinning_number)
if dinning_number > 8:
    print("Sorry, I don't have enough tables.")
else:
    print("We have enough tables.")

# 7.3

number = input("Please input an integer number:")
number = int(number)
if number % 10 == 0:
    print("The number can be divided by 10.")
else:
    print("The number cannot be divided by 10.")
