# 收集所有关键字参数，返回一个字典
def user_info(**kwargs):
    print(kwargs)


user_info(name="Alex", age=33, gender="male")
