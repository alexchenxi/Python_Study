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
print("🎬 电影院票价查询系统（输入 'quit' 退出）")
age_input = ""

while age_input.lower() != "quit":
    # 询问用户年龄（每次循环都获取新输入）
    age_input = input("\n请输入你的年龄（输入 'quit' 结束查询）：")

    # 1. 先判断是否要退出（此时条件测试已能终止，但这里跳过后续逻辑）
    if age_input.lower() == "quit":
        print("感谢使用，祝你观影愉快！👋")
        continue  # 跳过后续票价判断，直接进入下一次循环（条件测试会终止）

    # 2. 容错：处理非数字输入
    try:
        age = int(age_input)
    except ValueError:
        print(f"❌ 错误：'{age_input}' 不是有效的年龄，请输入数字或 'quit' 退出。")
        continue

    # 3. 容错：处理负数年龄
    if age < 0:
        print("❌ 错误：年龄不能为负数，请输入有效的年龄！")
        continue

    # 4. 根据年龄判断票价
    if age < 3:
        price = "免费 🆓"
    elif 3 <= age < 12:
        price = "10 美元 💰"
    else:
        price = "15 美元 💰"

    # 输出结果
    print(f"✅ 你的年龄是 {age} 岁，对应的票价为：{price}")
