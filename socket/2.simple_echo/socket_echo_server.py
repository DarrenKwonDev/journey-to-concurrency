import socket

LO = '127.0.0.1'
ACCEPT_ALL = '0.0.0.0'
PORT=6542 # ps -eo pid | grep 6542 로 확인 좀 해봐
MAX_CONN = 5

if __name__ == "__main__":
    server = socket.socket()
    server.bind((ACCEPT_ALL, PORT))
    server.listen(MAX_CONN) # __backlog는 connection 갯수 제한. 초과시 연결 거부

    try:
        while True:
            # blocking. Wait for an incoming connection. 
            # rmt_addr는 (연결한 클라의 ip, port)
            # conn은 또 다른 socket 객체임.
            print("blocking for waiting conn")
            conn, rmt_addr = server.accept() # connection 수립 대기
            print(conn, rmt_addr)
            print(conn.getpeername()) # raddr 출력. 즉, 이 conn에 연결된 클라이언트의 ip와 포트
            print(conn.getsockname()) # laddr 출력. 즉, 이 서버의 ip, port
            
            while True: # client로 부터 몇 개나 올 지 모르니까 계속 받아라
                # 영문자 숫자, 공백 1byte
                # 한글 등은 euc-kr 인코딩한 경우 2byte, utf-8 인 경우 3byte
                # 원래 encode해서 보내고 decode해서 받아야 하는데 alphanemeric하기만 하면 걍 해도 됨.
                b_data = conn.recv(1024) # bufsize 만큼 읽어라.
                if not b_data:
                    break
                print(b_data.decode('utf-8')) # 받을 때 decode
                
                conn.send(b_data + " 서버가 돌려줌".encode("utf-8")) # 보낼 때 encode

    except KeyboardInterrupt:
        server.close()