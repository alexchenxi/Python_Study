i = 0
while i < 5:
    print("hello")
    i += 1

# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
i = 1
sum = 0
while i <= 100:
    # if i % 2 == 0:
    sum += i if i % 2 == 0 else 0
    i += 1
print(sum)

j = 1
while j <= 5:
    if j == 3:
        print("skip this")
        j += 1
        continue
    print(f"Current step is {j}")
    j += 1

print("/n")

k = 1
while k <= 5:
    if k == 4:
        print("We will end this")
        break
    print(f"Current step is {k}")
    k += 1
