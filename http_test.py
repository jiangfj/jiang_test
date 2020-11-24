"""
http请求响应演示
"""
from socket import *

#　ＴＣＰ
s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

c,addr = s.accept() # 连接了客户端（浏览器）
print("Connect from",addr)

data = c.recv(1024 * 10) # 接收到了HTTP请求
print(data.decode())

# 组织响应格式
response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello world</h1>
"""

c.send(response.encode()) #　发送给浏览器

c.close()
s.close()
