s1 = "你好123abCD!@"
print(s1.encode())
print(s1.encode("utf-8"))
print(s1.encode("gbk"))

bytes = b"\xe4\xbd\xa0\xe5\xa5\xbd123abCD!@"
print(type(bytes))
print(bytes.decode())
