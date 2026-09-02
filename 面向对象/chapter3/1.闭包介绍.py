"""
在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数
使用外部函数变量的内部函数称为闭包
def 外部函数(外部参数):
  def 内部函数():
    使用外部函数的变量
  return 内部函数
"""


def func():
    num = 10
    return num


num = func()
print(num + 1)
