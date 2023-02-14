import socket

# FQDN(Fully Qualified Domain Name)
# 너 어디서 서빙하고 있어

print(socket.getfqdn()) # 이 코드 실행하는 기기. 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa

print(socket.getfqdn("kbs.co.kr")) # s3-website.ap-northeast-2.amazonaws.com
print(socket.getfqdn("naver.com")) # naver.com. 자체 서버
print(socket.getfqdn("sbs.co.kr")) # ec2-52-79-192-118.ap-northeast-2.compute.amazonaws.com
print(socket.getfqdn("youtube.com")) # nrt13s54-in-f14.1e100.net
print(socket.getfqdn("twitter.com")) # twitter.com. 자체 서버
print(socket.getfqdn("typed.do")) # 207.119.160.34.bc.googleusercontent.com
print(socket.getfqdn("aws.com")) # server-18-64-8-60.icn57.r.cloudfront.net