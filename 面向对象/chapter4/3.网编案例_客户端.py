"""
服务器端开发流程：
  1. 创建服务器端Socket对象
  2. 链接服务器端，指定：ip，端口号
  3. 接收信息并打印
  4. 给客户端发雄安锡
  5. 释放资源
"""

import socket

# 创建对象，ipv4 tcp
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("172.19.10.104", 10086))
print("Connected to server...")
data = client_socket.recv(1024).decode("utf-8")
print(data)
# 给客户端发送信息
client_socket.send(b"Hello This message is from client side!")
# 接受信息并打印
client_socket.close()
