# capitalize() title()
mystr2 = "this is a long sentence."
print(mystr2.capitalize())
print(mystr2.title())
print(mystr2.upper())

# lstrip()
mystr3 = "   Hello there   "
print(mystr3.lstrip())
print(mystr3.rstrip())
print(mystr3.strip())

# ljust() 左对齐填充 rjust center
mystr4 = "Alex"
print(mystr4.ljust(10, "."))
print(mystr4.center(10, "%"))
