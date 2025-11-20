# 8.9
standby_messages = ["Hello World", "Nice to meet you!", "Have a nice day!"]


def show_messages(list):
    for message in list:
        print(message)


show_messages(standby_messages)

print("###########################################")

# 8.10
# sent_messages = []


# def send_messages(list):
#     while list:
#         send_message = list.pop()
#         print(send_message)
#         sent_messages.append(send_message)


# send_messages(standby_messages)
# print(sent_messages)
# print(standby_messages)

# 8.11
sent_messages = []


def send_messages_new(list):
    while list:
        send_message = list.pop()
        print(send_message)
        sent_messages.append(send_message)


send_messages_new(standby_messages[:])
print(sent_messages)
print(standby_messages)
