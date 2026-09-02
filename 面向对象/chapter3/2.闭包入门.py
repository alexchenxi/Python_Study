"""
在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数
使用外部函数变量的内部函数称为闭包
def 外部函数(外部参数):
  外部函数的变量
  def 内部函数():
    使用外部函数的变量
  return 内部函数

1.函数名和函数名()，前者表示 函数对象，后者表示调用函数返回
"""


def outer(num):

    def inner(other):  # 有嵌套
        print(int(other) + num)  # 有引用

    return inner  # 有返回


inner = outer(10)
inner(20)
inner(20)
inner(20)
