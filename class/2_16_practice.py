import random

teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]

offices = [[], [], []]

for name in teachers:
    offices[random.randint(0, 2)].append(name)

for office in offices:
    print(f"办公室{offices.index(office) + 1}有{len(office)}个老师，他们分别是：")
    for name in office:
        print(f"{name}老师".rjust(7, " "))
    print()
