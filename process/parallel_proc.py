from concurrent.futures import process
from multiprocessing import Process, current_process
import time
import logging
import os

def proc_func(num):
    print(f"got {num} in {current_process().name}")
    time.sleep(1)
    pass

def main():
    parent_pid = os.getpid()
    logging.debug(f"main proc pid: {parent_pid}")

    processes = []

    for i in range(1, 31):
        p = Process(target=proc_func, name=f'{i}번 proc', args=(i, ))
        processes.append(p)
        p.start()
    
    for proc in processes:
        proc.join()
    
    logging.debug(f"main process exit")


if __name__ == '__main__':
    format = "%(asctime)s: [%(processName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    main()