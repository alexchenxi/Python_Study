# 8.1
def display_message():
    print("The topic of this chapter is Function.")


display_message()


# 8.2
def favorite_book(title):
    print(f"One of my favorite books is <<{title.title()}>>.")


favorite_book("GOne with the wind")


def describe_pet(animal_type, animal_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {animal_name.title()}")


describe_pet(animal_name="dahuang", animal_type="dog")
