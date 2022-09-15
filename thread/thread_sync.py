
import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os

"""
Thread synchronization (스레드 동기화)


"""

class FakeDataStore:
    def __init__(self):
        self.data = 0
        self._lock = threading.Lock()

    def update(self, thread_name):
        logging.debug(f"before {self.data}")
        # self.data란 변수는 store.update를 하면서 동시에 접근 가능한 메모리 영역이므로 race condition에 노출됨

        # 공유자원에 접근하는 Critical Section이므로 lock 걸자
        self._lock.acquire()

        
        logging.debug(f"thread {thread_name} has lock")

        local_copy = self.data # thread 바깥 변수를 stack frame 내로 값복사
        local_copy += 1 
        time.sleep(1)
        self.data = local_copy # 공유 자원 변수에 값복사

        self._lock.release() # 락 해제

        logging.debug(f"after {self.data}")
    
    def update2(self, thread_name):
        logging.debug(f"before {self.data}")

        # lock acquire, release를 with문으로 간단하게 표현 가능
        # https://docs.python.org/ko/3.10/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement
        with self._lock:
            logging.debug(f"thread {thread_name} has lock")

            local_copy = self.data # thread 바깥 변수를 stack frame 내로 값복사
            local_copy += 1 
            time.sleep(1)
            self.data = local_copy # 공유 자원 변수에 값복사

        logging.debug(f"after {self.data}")
        
        

if __name__ == '__main__':
    format = "%(asctime)s: [%(threadName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    store = FakeDataStore()

    logging.debug(store.data)

    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in ["a", "b", "c"]:
            executor.submit(store.update, i)

    logging.debug(store.data) # should be 3 
