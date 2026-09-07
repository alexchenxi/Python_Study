"""
服务器：
  1. 创建服务器socket对象
  2. 绑定ip和端口
  3. 设置最大监听数
  4. 等待客户端申请建立连接
  5. 读取客户端上传文件数据
  6. 读取到数据写到目的地文件中
  7. 释放资源
"""

import socket
from pathlib import Path

base_dir = Path(__file__).parent

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("172.19.10.104", 6666))

with open(base_dir / "data/test_pic.jpg", "rb") as src_f:
    # 循环读取数据
    while True:
        data = src_f.read(8192)
        client.send(data)
        if len(data) <= 0:
            break

print(f"客户端收到：{client.recv(1024).decode('utf-8')}")

client.close()
