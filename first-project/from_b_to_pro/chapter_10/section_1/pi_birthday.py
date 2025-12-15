from operator import indexOf
from pathlib import Path

contents = (Path(__file__).parent / "pi_minion.txt").read_text()
# contents_strip = contents.rstrip()
# lines = contents.splitlines()
# for line in lines:
#     print(line)

birthday = input("Please enter your birthday, in the from mmddyy：")
if birthday in contents:
    print(f"Your birthday is {birthday}, it appears in the first million digits of pi!")
    print(contents.find(birthday))
else:
    print("Your birthday does not appear in the first million digits of pi.")
