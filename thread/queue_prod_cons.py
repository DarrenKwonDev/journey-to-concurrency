"""
prod/cons와 pub/sub의 차이
- pub/sub
    - publisher가 데이터를 만들어서 쏘면 해당 topic을 구독한 모든 subscriber에게 전달
    - 1:N
- prod/cons
    - producer가 데이터를 만들어서 queue에 넣으면 consumer가 queue에서 데이터를 가져가서 처리. 
    - 즉, 할 일을 던지면 여러 worker중 하나가 가져가서 처리하는 방식
    - 1:1

근데 thread가 prod/cons가 무슨 상관임?
- multi thread design pattern의 대표격임.
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import random
import time
import threading
import queue

def producer(queue, event):
    while not event.is_set():
        item = random.randint(0, 256)
        queue.put(item)
        logging.debug(f'produce {item}')
        time.sleep(1)
    
    logging.debug('event flag set, exit')
    

def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        item = queue.get()
        logging.debug(f'consume {item}')
        time.sleep(1)

    logging.debug('event flag set, exit')

if __name__ == '__main__':
    format = "%(asctime)s: [%(threadName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    queue = queue.Queue(maxsize=10) # consumer의 throughput을 고려하여 적절한 queue size를 설정해야 함

    event = threading.Event() # thread간 통신을 위해 사용하는 event 객체로 flag용임.
    print(event.__dict__) # 최초 _flag: False

    with ThreadPoolExecutor(max_workers=3) as executor:
        # 본래 producer, consumer를 완전히 분리해야겠으나 여기서는 약식으로
        executor.submit(producer, queue, event) # producer thread

        executor.submit(consumer, queue, event) # consumer thread
    
        time.sleep(1)

        event.set() # 이벤트 발생, 여기선 프로그램 종료 flag로 활용한다.

    

