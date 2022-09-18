"""
pipe : https://docs.python.org/ko/3/library/multiprocessing.html#multiprocessing.Pipe

child process가 여러개라면 queue  
https://docs.python.org/ko/3/library/multiprocessing.html#multiprocessing.Queue
"""

import logging
from multiprocessing import Process, Pipe, current_process

def worker(num, conn):
    sub_total = 0
    for _ in range(num):
        sub_total += 1

    conn.send(sub_total)
    conn.close()

    print(f"{current_process().name} process, {sub_total}")

def main():
    parent_conn, child_conn = Pipe(duplex=False) # duplex=False : 단방향 통신

    p = Process(target=worker, args=(1000000, child_conn))
    p.start()
    p.join()

    print(f"{parent_conn.recv()}")

if __name__ == "__main__":
    format = "%(asctime)s: [%(processName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")
    
    main()