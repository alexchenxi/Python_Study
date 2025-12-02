def print_info(name, age, **user_info):
    print(f"{name.title()} is {age} years old.")
    if user_info:
        print(f"Here are other details about {name.title()}:")
        for info in user_info:
            print(f"His {info} is {user_info[info]};")
