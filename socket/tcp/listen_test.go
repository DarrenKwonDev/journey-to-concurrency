package tcp

import (
	"net"
	"testing"
)

func TestListener(t *testing.T) {
	// 해당 ip, port에 listener를 binding하였음. 
	// 다른 프로세스가 해당 ip, port를 사용할 수 없다는 말임.
	l, err := net.Listen("tcp", "127.0.0.1:0") 
	if err != nil {
		t.Fatal(err)
	}
	defer l.Close()

	t.Logf("bound to %q", l.Addr())
}