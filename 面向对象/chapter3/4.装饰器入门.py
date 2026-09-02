"""
装饰器：
  概述：作用
    本质是一个闭包函数，目的是，在不改变原有函数的基础上，对齐功能做增强
  前提条件：
    1. 有嵌套
    2. 有引用
    3. 有返回
    4. 有额外功能
  写法：
    1.装饰后的函数名=装饰器名（被装饰的函数）
    2. 语法糖 @装饰器名在函数上面
"""


# 1.定义外部函数，形参列表接收 要被装饰的函数对象
def check_login(fn):
    # 2. 定义内部函数
    def fn_inner():
        # 访问原函数
        print("登录中")
        fn()

    return fn_inner


@check_login
def commit():

    print("发表评论")


# cn = check_login(commit)
# cn()

commit()
