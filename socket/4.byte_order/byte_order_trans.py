import socket

# 바이트 순서를 바꿔주는 변환 함수들
# htonl htons ntohl ntohs
# h : host
# n : network
# s : short
# l : long
# htonl -> host to network long
# htons -> host to network short
# ntohl -> network to host long
# ntohs -> network to host short

# intel cpu, m1 cpu는 little endian 쓴다네
# Note Both Apple silicon and Intel-based Mac computers use the little-endian format for data

print(socket.ntohl(4738854)) # NBO에 따른 숫자가 들어왔는데 이걸 호스트 컴퓨터에 맞게 바꿔. (호스트도 빅-엔디안이면 아무 일도 하지 않음)
print(socket.htonl(642729984)) # HBO에 따른 숫자를 NBO로 바꿔.
