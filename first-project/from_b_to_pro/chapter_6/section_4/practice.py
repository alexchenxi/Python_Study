# 6.7
people = [{"first_name": "Alex", "last_name": "Zhang", "age": 37, "city": "Suzhou"},
          {"first_name": "Steven", "last_name": "Zhou", "age": 47, "city": "Hongkong"},
          {"first_name": "Tina", "last_name": "Wang", "age": 27, "city": "Shanghai"}]
for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old, living in {person['city']}")

print("################################")
# 6.8
pets = [{"type": "Husky", "master": "Li Lei"}, {"type": "Teddy", "master": "Han Meimei"},
        {"type": "British Shorthair", "master": "Mary Jane"}]
for pet in pets:
    print(f"{pet['type']} is belong to {pet['master']}")

print("################################")

# 6.9
favourite_places = {'Alex': ['Beijing', "Tokyo", "LA"], 'Bob': ['New York', 'London', 'Paris'],"Chris":['Moscow']}
for person, places in favourite_places.items():
    if len(places) > 1:print(f"{person}: \"My favourite places are:")
    else:
        print(f"{person}: \"My favourite place is:")
    for place in places:
            print(f"\t{place}")
