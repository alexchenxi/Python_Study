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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 6666))

server.listen(5)

print("serving...")
accpet_socket, client_info = server.accept()


with open(base_dir / "data/my.txt", "wb") as des_f:
    # 循环读取数据
    while True:
        bys = accpet_socket.recv(8192)  # 18kb
        if len(bys) <= 0:
            break
        des_f.write(bys)

accpet_socket.send("文件接收成功！")

accpet_socket.close()
