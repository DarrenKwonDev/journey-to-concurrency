import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os

"""
ThreadPoolExecutor
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

        print(list(tasks))

