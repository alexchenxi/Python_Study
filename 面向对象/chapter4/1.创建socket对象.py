"""
网络编程介绍：
    概述：
        也叫网络通信，Socket通信，即：通信双方都独有自己的Socket对象
        数据通过Socket之间通过 数据报包(udp协议) 或者 字节流(TCP协议)的形式进行传输。
    白话：
        你和远处的人交流，看似两个再交互，实则通过两部手机来交互
"""

import socket

# 参数1：Address Family 地址族，即IPV4 IPV6 （AF_INET6）
# 参数2：Socket Type，SOCK_STREAM(tcp) SOCK_DGRAM(UDP)
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)
