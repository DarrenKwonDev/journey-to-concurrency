import socket


print(socket.gethostbyname("kbs.co.kr")) # 52.219.202.60
print(socket.gethostbyname("52.219.202.60")) # 52.219.202.60. ip 번호를 줬으니 그대로 반환함.
print(socket.gethostbyname("twitter.com")) # 104.244.42.193