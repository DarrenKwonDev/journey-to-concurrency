import socket

from socket_echo_server import LO, PORT

client = socket.socket()
client.connect((LO, PORT))

client.send(b"hello from client\n") # b for bytes. 영어만 있어서 이래도 됨.
client.send("한글 wow".encode("utf-8")) # send할 때 encode

b_data = client.recv(2 ** 10)
print(b_data.decode("utf-8")) # recv할 때 decode

client.close()