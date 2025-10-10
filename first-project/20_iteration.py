# 高斯累计加法
total = 0
for i in range(1, 101):
    total = total + i
print(total)

score = {"101": 66, "102": 99, "103": 45}
print(type(score))
for i in score:
    if score[i] < 60: print(i)
