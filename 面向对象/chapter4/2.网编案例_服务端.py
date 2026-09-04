"""
服务器端开发流程：
  1. 创建服务器端Socket对象
  2. 绑定IP地址和端口
  3. 设置最大监听数
  4. 等待客户端链接
  5. 给客户端发送消息
  6. 接收客户端信息并打印
  7. 释放资源
"""

import socket

# 创建对象，ipv4 tcp
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip地址，端口号
sever_socket.bind(("172.19.10.104", 10086))
# 设置最大监听数
sever_socket.listen(5)
print("servering...")
# 等待客户端建立链接
accept_socket, client_info = sever_socket.accept()
print("client connected...")
# 给客户端发送信息
accept_socket.send(b"Welcome to visit server!")
# 接受信息并打印
data = accept_socket.recv(1024).decode("utf-8")
print(f"收到来自{client_info}的信息：{data}")
accept_socket.close()
