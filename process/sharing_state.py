"""
process는 thread와 달리 memory 상 data, code, stack, heep 모두 다르다.
즉, 프로세스는 서로 데이터를 공유하지 않기 때문에 상태 공유를 위한 별도의 로직이 필요하다.
https://docs.python.org/ko/3/library/multiprocessing.html#sharing-state-between-processes
https://docs.python.org/ko/3/library/multiprocessing.shared_memory.html
"""
import logging
from multiprocessing import Process, current_process, Value

# 프로세스 메모리 공유 예제
def generate_update_number(shared_value):
    for _ in range(50):
        shared_value.value += 1
    
    print(current_process().name, "data", shared_value.value)

def main():
    process_list = []
    share_value = Value('i', 0) 

    for _ in range(1, 11):
        p = Process(target=generate_update_number, args=(share_value, ))
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join() # 다른 프로세스가 끝날 때 까지 기다려.
    
    print(share_value.value) # 500

if __name__ == '__main__':
    format = "%(asctime)s: [%(processName)s] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    main()
