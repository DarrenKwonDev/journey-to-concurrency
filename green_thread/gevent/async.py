import gevent
import random

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous() # 실행 순서 보장. 하나 끝나고 하나 시작하는 방식이라 느림

print('Asynchronous:')
asynchronous() # 실행 순서 보장 안됨. 단 서로 작업에 간섭이 없고 서로 block하지 않아서 빠름

