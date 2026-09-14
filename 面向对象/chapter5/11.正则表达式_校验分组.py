import re

fruits = ["apple", "banana", "orange", "pear"]
for fruit in fruits:
    if re.match("apple|pear", fruit):
        print(f"喜欢吃{fruit}")
    else:
        print(f"不喜欢吃{fruit}")
