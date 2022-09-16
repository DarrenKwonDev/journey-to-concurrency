
from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request
from multiprocessing import Process, current_process
import logging

URLS = [
    "https://www.python.org",
    "https://www.google.com",
]

def proc_func(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        for _ in URLS:
            future_dict = {executor.submit(proc_func, url, 60): url for url in URLS}

        for finished_future in as_completed(future_dict):
            try:
                # 결과
                data = finished_future.result()
                print('%d bytes' % (len(data)))
            except Exception as e:
                logging.exception(e)

if __name__ == '__main__':
    format = "%(asctime)s: [%(processName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    main()
