import re

# result = re.match(".it", "ait")
# result = re.match("\.it", ".it")
result = re.match("[abc]de", "ade")
result = re.match("[^abc]fg", "dfg")
result = re.match("[3-7]86", "486")

result = re.match("a\\dhm", "a2hm")
result = re.match("a\\Dhm", "a!hm")

result = re.match("a\\shm", "a hm")
result = re.match("a\\shm", "a\thm")  # 成功
# result = re.match("a\\shm", "a\nhm")  # 成功

# \\w [a-zA-Z0-9_]
if result:
    print(result.group())
else:
    print("no matches!")
