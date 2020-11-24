"""
poll IO 多路复用方法处理
"""
from socket import *
from select import *

# 准备几个IO对象
tcp_socket = socket()
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

file = open("../day16/my.log","rb")

# 监控IO
p = poll() # 生成poll对象

# 关注监听套接字读行为
p.register(tcp_socket,POLLIN)
p.register(udp_socket,POLLOUT)
p.register(file,POLLOUT)

# 建立找对象的关系地图 必须和关注的IO保持一直
map = {
    tcp_socket.fileno():tcp_socket,
    udp_socket.fileno():udp_socket,
    file.fileno():file
}

# 开始监控
print("开始监控IO啦")
events = p.poll()
print(events) # [(3, 1)] [(4, 4), (5, 4)]

# 处理IO行为
map[3].accept()

p.unregister(4)


