package tcp

import (
	"io"
	"net"
	"testing"
)

func TestDial(t *testing.T) {
	// server side
	// Create a listener on a random port.
	listener, err := net.Listen("tcp", "127.0.0.1:")
	if err != nil {
		t.Fatal(err)
	}

	done := make(chan struct{})

	go func() {
		defer func() { done <- struct{}{} }()

		for {
			conn, err := listener.Accept() // client와 tcp connection 수립
			if err != nil {
				t.Log(err)
				return
			}

			// handler
			go func(c net.Conn) {
				defer func() {
					c.Close()
					done <- struct{}{}
				}()

				buf := make([]byte, 1024)
				for {
					n, err := c.Read(buf)
					if err != nil {
						if err != io.EOF { // FIN 패킷을 받고 나면 io.EOF 반환함.
							t.Error(err)
						}
						return
					}

					t.Logf("received: %q", buf[:n])
				}
			}(conn)
		}
	}()

	// client side
	conn, err := net.Dial("tcp", listener.Addr().String())
	if err != nil {
		t.Fatal(err)
	}

	conn.Close() // client에서 close를 요청. FIN 패킷 보냄
	<-done

	listener.Close() 
	<-done
}
