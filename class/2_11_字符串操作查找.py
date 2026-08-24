mystr = "Get fucking off you bastard peeking my screen!"

# find rfind 找不到返回-1
print("find", mystr.find("fucking"))
print("rfind", mystr.rfind("peeking"))

# index rindex 找不到报错
print("index", mystr.index("fucking"))
print("rindex", mystr.rindex("peeking"))

# count
print("count", mystr.count("ing"))

# startswith, endswith True/False
