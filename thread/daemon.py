import logging
import time
import threading
import os

"""
daemon
메인 스레드가 종료되면 자식 스레드도 종료되도록 하는 속성
보통 메인 스레드를 while True 걸어놓고 종료되지 않게 한 다음 daemon thread를 활용하는 경우가 많다
"""

if __name__ == '__main__':
    format = "%(asctime)s: [%(threadName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    def worker1(name: str):
        logging.debug(f'{name} start')
        time.sleep(2)
        logging.debug('end')

    def worker2(name: str):
        logging.debug(f'{name} start')
        time.sleep(1)
        logging.debug('end') 

    t1 = threading.Thread(target=worker1, args=("worker1", ), daemon=True)
    t2 = threading.Thread(target=worker2, args=("worker2", ), daemon=True)

    t1.start()
    t2.start()

    # daemon이 끝나지 않음. 
    # 만약, 이 코드가 없다면 sub daemon thread들이 완료되기 전에 main thread가 exit하면서 모든 thread가 종료된다
    while 1:
        logging.debug('main code never done')
        pass
        
