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

    def main():
        pass

    def task(name):
        time.sleep(1)
        return f'{name} done'

    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ["task1", "task2", "task3"])

        print(list(tasks))

