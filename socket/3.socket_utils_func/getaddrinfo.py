import socket

# 이 도메인에 이 포트에 무슨 소켓 통신이 가능함?
# 추가적으로 인자를 주면 이 범위를 좀 더 좁힐 수 있음.
res = socket.getaddrinfo("kbs.co.kr", 80)

sock = socket.socket(*res[0][:3]) # family, type, proto
print(sock)