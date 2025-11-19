# un_users = ["alex", "bob", "chris"]
# confirmed_users = []
# while un_users:
#     user = un_users.pop()
#     print(f"Verifying user: {user.title()}")
#     confirmed_users.append(user)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# responses = {}
# active = True

# while active:
#     name = input("Please input your name.")
#     response = input("Which city would you like to visit?")

#     responses[name] = response

#     repeat = input("Would you like to let another person to respond? (yes/no)")
#     if repeat.lower() == "no":
#         active = False

# print("\n<---Results--->")
# for res in responses:
#     print(f"{res.title()} would like to visit {responses[res]}")


# 7.8
# sandwich_orders = [
#     "pastrami",
#     "original_favor",
#     "double_cheese",
#     "pastrami",
#     "pastrami" "meat feast",
# ]
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich}")
#     finished_sandwiches.append(sandwich)
# result = ""
# for sandwich in finished_sandwiches:
#     result += f'"{sandwich}" '
# print(f"Now {result} have been made.")

# 7.9
# sandwich_orders = [
#     "pastrami",
#     "original_favor",
#     "double_cheese",
#     "pastrami",
#     "pastrami" "meat feast",
# ]
# print("Sorry pastrami sold out...")
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich}")
#     finished_sandwiches.append(sandwich)
# result = ""
# for sandwich in finished_sandwiches:
#     result += f'"{sandwich}" '
# print(f"Now {result} have been made.")


# 7.10
flag = True
responses = {}
while flag:
    user = input("Please input your name: ")
    resort = input("If you could visit one place in the world, where would you go? ")
    responses[user] = resort
    repeat = input("Would you like to let another person to respond? (yes/no)")
    if repeat.lower() == "no":
        flag = False
for res in responses:
    print(f"{res.title()} would like to visit {responses[res].title()}.")
