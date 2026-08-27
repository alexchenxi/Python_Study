info = [
    {"name": "Alex", "age": 33, "phone": "18514002233"},
    {"name": "Rose", "age": 22, "phone": "13514002233"},
    {"name": "Bob", "age": 18, "phone": "16514002233"},
]

info.sort(key=lambda x: x["name"])
print(info)

info.sort(key=lambda x: x["age"], reverse=True)
print(info)
