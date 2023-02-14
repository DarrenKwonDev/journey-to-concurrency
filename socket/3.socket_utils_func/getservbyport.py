import socket

# 포트를 주면 해당 포트를 사용하는 프로토콜을 반환함.
# 즉, getservbyname의 반대임.

print(socket.getservbyport(80)) # http
print(socket.getservbyport(443)) # https
print(socket.getservbyport(5432)) # postgresql

