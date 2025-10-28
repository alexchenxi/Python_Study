# 5.8
user_list = ["admin", "Jacky", "Rose", "Alex", "Trump"]
for user in user_list:
    if user == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again。")

print("################################")

# 5.9
user_list = []
if len(user_list) == 0:
    print("We need to find some users")
else:
    for user in user_list:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again。")

print("################################")

# 5.10
current_users = ["Jacky", "Rose", "Alex", "Trump", "Michael", "DaVid"]
new_users = ["roSe", "Allen", "David", "Hakeen"]

# 列表推导式
current_users_lower = [item.lower() for item in current_users]

print(current_users_lower)
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Sorry, user "{user}" has been used, please input another user name')
    else:
        print(f'"{user}" has not been used!')


print("################################")

# 5.11
# list列表和range序列是有区别的，range不可增删改，元素类型只能是整数，只可以遍历/长度，内存效率极高
numbers = list(range(1, 10))
print(numbers)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
