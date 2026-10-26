

# 登录 得到COOKIE
# 带着COOKIE 发送请求，获取数据

# 必须把上面两个操作连起来
# 使用SESSION进行请求-》SESSION是一连串的请求，在这个过程中cookies不会丢失
import requests

session=requests.session()
