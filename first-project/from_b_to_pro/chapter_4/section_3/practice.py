# 4.3
for num in range(1, 21):
    print(num)
print("########################")

# 4.4
# for num in range(1, 1000_001):
#     print(num)

# 4.5
arr = list(range(1, 1000_001))
print(min(arr))
print(max(arr))
print(sum(arr))

# 4.6
odd = list(range(1, 21, 2))
print(odd)

# 4.7
threes = list(range(3, 31, 3))
print(threes)

# 4.8
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

# 4.9
cubes_comprehension = [value**3 for value in range(1, 11)]
for num in cubes:
    print(num)
