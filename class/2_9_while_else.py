# while-else 只有while部分的循环走完，才会执行到else部分的逻辑,所以一般和break组合使用
# for-else 同理

i = 1
while i <= 5:
    print("Loading...")
    if i == 3:
        print("Network Error")
        break
        # i += 1
        # continue
    i += 1
else:
    print("Load Complete!")
