# 6.1
person = {"first_name": "Alex", "last_name": "Zhang", "age": 37, "city": "Suzhou"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

# 6.2
favourate_numbers = {"Alex": 23, "Bob": 32, "Chris": 41, "Nikola": 15, "Kevin": 7}
print(f"Alex's favourate number is {favourate_numbers["Alex"]}")
print(f"Bob's favourate number is {favourate_numbers["Bob"]}")
print(f"Chris's favourate number is {favourate_numbers["Chris"]}")
print(f"Nikola's favourate number is {favourate_numbers["Nikola"]}")
print(f"Kevin's favourate number is {favourate_numbers["Kevin"]}")

# 6.3
coding_terms = {"range": "序列", "list": "列表", "print": "打印"}
print(f"range: {coding_terms['range']}")
print(f"list: {coding_terms['list']}")
print(f"print: {coding_terms['print']}")

print("range" + "\n" + f"\t{coding_terms['range']}")
print("list" + "\n" + f"\t{coding_terms['list']}")
print("print" + "\n" + f"\t{coding_terms['print']}")
