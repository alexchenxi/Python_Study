# 接收所有位置参数，返回一个元组
def user_info(*args):
    print(type(args))


user_info("alex", 22, "male")
