import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os

"""
ThreadPoolExecutor

내부 구현을 보면 생각보다 단순한 편이니 꼭 읽어보자

내부 구현 살펴보면 max_workers의 제한이 아래와 같다.
if max_workers is None:
    # ThreadPoolExecutor is often used to:
    # * CPU bound task which releases GIL
    # * I/O bound task (which releases GIL, of course)
    #
    # We use cpu_count + 4 for both types of tasks.
    # But we limit it to 32 to avoid consuming surprisingly large resource
    # on many core machine.
    max_workers = min(32, (os.cpu_count() or 1) + 4)

내부적으로 _work_queue에 _WorkItem을 넣어서 관리한다. 
"""

if __name__ == '__main__':
    format = "%(asctime)s: [%(threadName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    print(f"main pid: {os.getpid()}")

    def task(name):
        logging.debug(f"sub thread native id: {threading.get_native_id()}")
        time.sleep(1)
        return f'{name} {threading.get_native_id()} done'

    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ["task1", "task2", "task3"])

        print(list(tasks)) # return thread return value

