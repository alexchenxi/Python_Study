# 7.4
# prompt = input("Please enter one topping for your pizza, enter \"quit\" to quit: ")
# while prompt != "quit":
#     print(f"Okay, we will add {prompt} to your pizza.")
#     prompt = input("Please enter one topping for your pizza, enter \"quit\" to quit: ")

# while True:
#     prompt = input("Please enter one topping for your pizza, enter \"quit\" to quit: ")
#     if prompt == "quit":
#         print("Goodbye")
#         break
#     else:
#         print(f"Okay, we will add {prompt} to your pizza.")

# 7.5
# break退出循环，创建一个无线循环的条件，通过break结束
# while True:
#     age = input("Please tell me age of you, enter \"quit\" to quit: ")
#     if age.lower() == "quit":
#         print("Goodbye")
#         break
#
#     try:
#         age = int(age)
#     except ValueError:
#         print(f"❌ Error：'{age}' is not a valid age, please input integer or 'quit'.")
#         continue
#     if int(age) < 0:
#         print("Sorry, you can't enter negative numbers.")
#         continue
#
#     if int(age) < 3:
#         price = "Free"
#     elif 3 <= int(age) <= 12:
#         price = "$10"
#     else:
#         price = "$15"
#
#     print(f"Your age is {age} years old, and your price is: {price}.")

# 7.6
# 条件判断结束循环，满足某条件才会执行核心代码
# print("🎬 电影院票价查询系统（输入 'quit' 退出）")
# prompt = "Please input your age, press 'quit' to quit."
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message.lower() != "quit":
#         try:
#             age = int(message)
#         except ValueError:
#             print(f"❌ 错误：'{message}' 不是有效的年龄，请输入数字或 'quit' 退出。")
#             continue
#         price = ""
#         if age < 3:
#             price = "免费 🆓"
#         elif 3 <= age < 12:
#             price = "10 美元 💰"
#         else:
#             price = "15 美元 💰"
#         print(f"Your age is {age} years old, and your ticket is ${price}")

# active做为循环标志，False时停止循环
print("🎬 电影院票价查询系统（输入 'quit' 退出）")
prompt = "Please input your age, press 'quit' to quit."
active = True
while active:
    message = input(prompt)
    if message.lower() == "quit":
        active = False
    else:
        try:
            age = int(message)
        except ValueError:
            print(f"❌ 错误：'{message}' 不是有效的年龄，请输入数字或 'quit' 退出。")
            continue
        price = ""
        if age < 3:
            price = "免费 🆓"
        elif 3 <= age < 12:
            price = "10 美元 💰"
        else:
            price = "15 美元 💰"
        print(f"Your age is {age} years old, and your ticket is {price}")
