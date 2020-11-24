"""
基于 poll 的 IO并发模型
"""

from socket import *
from select import *

# 创建全局变量
HOST = "0.0.0.0"
PORT = 8800
ADDR = (HOST, PORT)

# 创建套接字
sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

# IO多路复用往往与非阻塞IO一起使用，防止传输过程的卡顿
sockfd.setblocking(False)

# 创建poll对象
p = poll()
# 关注的IO
p.register(sockfd, POLLIN)

# 建立文件描述符查找对象的字典
map = {sockfd.fileno(): sockfd}

# 循环监控关注的IO
while True:
    events = p.poll() # events--> [(fileno,event),()]
    # 对监控的套接字就绪情况分情况讨论
    for fd,event in events:
        if fd == sockfd.fileno():
            # 处理客户端连接
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 连接一个客户端就多监控一个
            connfd.setblocking(False)
            p.register(connfd,POLLIN|POLLERR)
            map[connfd.fileno()] = connfd # 维护字典
        elif event==POLLIN:
            # 某个客户端连接套接字就绪
            data = map[fd].recv(1024).decode()
            # 客户端退出
            if not data:
                p.unregister(fd)  # 删除监控
                map[fd].close()
                del map[fd] # 维护字典删除一项
                continue
            print(data)
            # map[fd].send(b'OK') # 直接回复消息
            p.register(fd,POLLOUT) # 关注写
        elif event == POLLOUT:
            # 写处理
            map[fd].send(b"OK")
            p.register(fd,POLLIN) # 重新关注读
