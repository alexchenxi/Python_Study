def check_login(fn):
    def fn_inner():
        print("检测登录中。。。")
        fn()

    return fn_inner


def check_code(fn):
    def fn_inner():
        print("验证码通过")
        fn()

    return fn_inner


def my_decorator(fn):
    def fn_inner():
        print("加载中...")
        fn()

    return fn_inner


# 语法糖：从上到下顺序
# @check_login
# @check_code
def commit():
    print("发表评论。。。。")


# 传统写法 由内到外
check_login(check_code(commit))()

# commit()
