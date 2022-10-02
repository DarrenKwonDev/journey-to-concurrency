package tcp

import (
	"net"
	"syscall"
	"testing"
	"time"
)

func DialTimeout(
	network, address string, timeout time.Duration,
) (net.Conn, error) {

	// create Dialer struct with timeout
	d := net.Dialer{
		Control: func(_, addr string, _ syscall.RawConn) error {
			return &net.DNSError{
				Err:         "connection timed out",
				Name:        addr,
				Server:      "127.0.0.1",
				IsTimeout:   true,
				IsTemporary: true,
			}
		},
		Timeout: timeout,
	}
	return d.Dial(network, address)
}

func TestDialTimeout(t *testing.T) {
	// private 대역대이므로 connection에 실패할 것으로 예상
	c, err := DialTimeout("tcp", "10.0.0.1:http", 5*time.Second)

	if err == nil {
		c.Close()
		t.Fatal("connection did not time out")
	}

	nErr, ok := err.(net.Error) // net.Error type casting should be success
	if !ok {
		t.Fatal(err)
	}
	if !nErr.Timeout() {
		t.Fatal("error is not a timeout")
	}
}
