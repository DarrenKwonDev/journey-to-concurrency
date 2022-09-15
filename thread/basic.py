import logging
import time
import threading
import os

if __name__ == '__main__':
    format = "%(asctime)s: [%(threadName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    logging.debug(f"main pid: {os.getpid()}")

    def worker1():
        logging.debug(f"worker 1 pid: {os.getpid()}") # should be the same as main
        time.sleep(1)
        logging.debug('end')

    def worker2():
        logging.debug(f"worker 2 pid: {os.getpid()}") # should be the same as main
        time.sleep(5)
        logging.debug('end')

    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()

    logging.debug('main code passed, in background, worker alive')

