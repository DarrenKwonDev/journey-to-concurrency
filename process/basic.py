
from multiprocessing import Process
import time
import logging
import os

def proc_func(name):
    # logging이 아닌 print임에 주의. 
    print(f"Process {name} pid: {os.getpid()}") 
    time.sleep(3)

def main():
    logging.debug(f"main proc pid: {os.getpid()}")
    p = Process(target=proc_func, args=("a", ))

    p.start()

    p.join() # wait until process terminated

    logging.debug(f"main process exit. child proc is {p.is_alive()}")


if __name__ == '__main__':
    format = "%(asctime)s: [%(processName)s] %(message)s" # https://docs.python.org/ko/3/library/logging.html#logrecord-attributes
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    main()

    

