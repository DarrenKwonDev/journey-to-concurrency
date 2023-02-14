import socket


# OSI 3(인터넷), 4계층(전송)의 protocol을 적어주면 proto를 반환
# 3: ip, icmp
# 4: tcp, udp

tcp_proto = socket.getprotobyname("tcp")

socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=tcp_proto)
