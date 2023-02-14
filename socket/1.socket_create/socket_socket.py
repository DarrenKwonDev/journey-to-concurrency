# https://docs.python.org/3/library/socket.html
import socket

# family, type, proto, fileno
sock = socket.socket(
    family=socket.AF_UNIX, 
    type=socket.SOCK_STREAM)
print(sock)