import socket

# 응용 계층(7계층)에 있는 프로토콜을 주면 사용하는 포트를 반환함
print(socket.getservbyname("http")) # 80
print(socket.getservbyname("http", "tcp")) # 80
print(socket.getservbyname("https")) # 443
print(socket.getservbyname("pop3")) # 110
print(socket.getservbyname("telnet")) # 23
print(socket.getservbyname("ssh")) # 22
print(socket.getservbyname("ftp")) # 21
print(socket.getservbyname("ftps")) # 990
print(socket.getservbyname("smtp")) # 25

