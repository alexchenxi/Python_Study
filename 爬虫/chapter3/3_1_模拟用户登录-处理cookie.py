# 登录 得到COOKIE
# 带着COOKIE 发送请求，获取数据

# 必须把上面两个操作连起来
# 使用SESSION进行请求-》SESSION是一连串的请求，在这个过程中cookies不会丢失
import requests

session = requests.session()
data = {"loginName": "12321321", "password": "abcd1234"}

# 1.登录
url = "https://passport.17k.com/cd/user/login"
resp = session.post(url, data=data)
# print(resp.text)
print(resp.cookies)


# 2.拿数据
resp = session.get(
    "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919",
    headers={"Cookie": "GUID=xxxx"},
)
