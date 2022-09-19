from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import threading
import requests
import time

def performance(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} took {duration} seconds")
        return result
    return wrapper

"""
sync blocking하게 일반 요청을 보내는 경우
"""
@performance
def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            with session.get(url) as response:
                print(f"[{response.status_code}] Read {len(response.content)} from {url}")

"""
multi threading
io bound 작업에는 요청 대기에 따른 유휴 시간 때문에 GIL에도 불구 threading이 효율적.
각 스레드가 요청을 개별적으로 처리하기 때문에 순서를 보장할 수 없음.
"""
# https://docs.python.org/ko/3/library/threading.html#thread-local-data
thread_local = threading.local()

@performance
def request_multi_thread(urls):

    # 같은 thread에서는 session 객체를 재생성하지 않고 재사용하기 위함
    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    def request_site(url):
        session = get_session()

        with session.get(url) as response:
            print(f"[{response.status_code}] Read {len(response.content)} from {url}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(request_site, urls)


"""
multi process
여러 프로세스를 띄운다는 것은 사실상 해당 프로그램을 fork해서 여러대 돌리는 것과 같은 이치이다.  
그리고 python에서는 해당 프로세스에 전달하는 함수나 변수들은 pickling되어 전달되는 것으로 보인다. 
"""
# https://stackoverflow.com/questions/52722362/how-to-assign-python-requests-sessions-for-single-processes-in-multiprocessing-p
# sub process는 main process와의 별도의 메모리 공간을 사용하므로 전역 변수처럼 선언해도 어차피 process마다 다른 값을 사용하게 된다.
session = None

def init_process():
    global session # process내에서 initializer와 실행되는 함수 내의 변수를 공유하기 위함
    if not session:
        session = requests.Session()

def request_site(url):
    with session.get(url) as response:
        print(multiprocessing.current_process().name)
        print(f"[{response.status_code}] Read {len(response.content)} from {url}")

@performance
def request_multi_process(urls):
    with multiprocessing.Pool(initializer=init_process, processes=4)as pool:
        pool.map(request_site, urls)

def main():
    urls = [
        "https://www.producthunt.com/",
        "https://www.tensorflow.org/"
        "https://www.python.org/",
        "https://www.google.com/",
        "https://www.facebook.com/",
        "https://www.youtube.com/",
        "https://www.amazon.com/",
        "https://www.twitter.com/",
        "https://www.linkedin.com/",
    ] * 3

    request_all_sites(urls)
    request_multi_thread(urls)
    request_multi_process(urls)


if __name__ == "__main__":
    main()