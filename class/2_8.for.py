for i in "Hello World":
    if i.upper() == "O":
        # print("遇到o跳出循环")
        print("遇到o不打印", end=" ")
        # break
        continue
    print(i, end=" ")
