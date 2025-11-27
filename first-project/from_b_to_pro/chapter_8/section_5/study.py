def make_pizza(*tappings):
    """pizza to be made"""
    print("\nMaking a pizza with the following toppings:")
    for tapping in tappings:
        print(f"- {tapping}")


make_pizza("cheese", "onion", "paperonni")

print("##########################")


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


alex = build_profile("Alex", "Zhang", location="Suzhou", field="It")

print(alex)
