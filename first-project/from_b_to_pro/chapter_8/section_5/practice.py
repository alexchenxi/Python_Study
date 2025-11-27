# 8.12
def order_sandwich(*fillings):
    print(f"\nThe fillings of your sandwich are:")
    for filling in fillings:
        print(f"- {filling}")


order_sandwich("cheese", "cucumber", "turkey")
print("##################")


# 8.13
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


alex = build_profile("Alex", "Zhang", location="Suzhou", field="It", age=37)
print(alex)
print("##################")


# 8.14
def make_car(brand, model, **car_info):
    car_info["brand"] = brand
    car_info["model"] = model
    return car_info


car = make_car("Nissan", "Altima", color="pearl", turbo=True)

print(car)
