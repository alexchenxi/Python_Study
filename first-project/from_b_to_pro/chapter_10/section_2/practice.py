# 10.4
from pathlib import Path

# guest = input(f"Please input your name:")
# file = Path("guest.txt")
# if file.exists():
#     contents = file.read_text().rstrip()
#     contents += f" {guest.title()}"
#     file.write_text(contents)
# else:
#     file.write_text(guest.title())

# 10.5
file_book = Path("guest_book.txt")

flag = True
string = ""
while flag:
    result = input(f"Please input your name, ending with \"quit\"")
    if result == "quit":
        flag = False
    else:
        string += result.title() + " "
file_book.write_text(string)
