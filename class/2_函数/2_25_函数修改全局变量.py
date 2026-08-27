a = 100
print(a)


def testA():
    print(a)


def testB():
    global a
    a = 200
    print(a)


testA()
testB()
print(a)

"""
    总结：
        1. 如果在函数里面直接赋值a=200,此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
        2. 函数体内部修改全局变量：global声明a为全局变量，然后再重新赋值
"""
