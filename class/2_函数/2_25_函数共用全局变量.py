a = 0


def testA():
    print(a)


def testB():
    global a
    a = 100
    print(a)


testA()
testB()
testA()
