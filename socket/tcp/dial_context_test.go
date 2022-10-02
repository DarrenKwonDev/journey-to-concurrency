package tcp

import (
	"context"
	"net"
	"syscall"
	"testing"
	"time"
)

func TestDialContext(t *testing.T) {
	dl := time.Now().Add(5 * time.Second) // deadline
	ctx, cancel := context.WithDeadline(context.Background(), dl)
	defer cancel()

	var d net.Dialer // DialContext is a method on a Dialer
	d.Control = func(_, _ string, _ syscall.RawConn) error {
		// deadline 5초 동안 tcp connection 수립을 하지 않으므로 DialContext에 전달된 context가 complete되고 이에 따라 Dial은 error 뱉고 끝남.
		time.Sleep(5 * time.Second + time.Millisecond)
		return nil
	}

	// context expires before the connection is complete, an error is returned. 
	// Once successfully connected, any expiration of the context will not affect the connection.
	conn, err := d.DialContext(ctx, "tcp", "10.0.0.0:80")
	if err == nil {
		conn.Close()
		t.Fatal("connection did not time out")
	}

	nErr, ok := err.(net.Error)
	
	t.Log(nErr) // should be i/o timeout

	if !ok {
		t.Error(err)
	} else {
		if !nErr.Timeout() {
			t.Errorf("error is not a timeout: %v", err)
		}
	}

	if ctx.Err() != context.DeadlineExceeded {
		t.Errorf("expected deadline exceeded; actual: %v", ctx.Err())
	}
}
