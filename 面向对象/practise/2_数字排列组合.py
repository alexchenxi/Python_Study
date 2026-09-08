"""
需求：
  1.要求1，2，3，4同时包括
  2. 13不挨着
  3. 数字4不开头
  4. 5行代码以内

"""

count = 0
for i in range(1234, 4322):
    s = str(i)

    if (
        "1" in s
        and "2" in s
        and "3" in s
        and "4" in s
        and "13" not in s
        and s[0] != "4"
    ):
        count += 1
        print(s, end="\n" if count % 5 == 0 else "\t")
print()
print(f"一共{count}个组合")
